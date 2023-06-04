import subprocess


class Ping:
    def __init__(self, hostname_or_ip, count):
        print('here')
        self.ping_data = subprocess.run(
            ["ping", "-c", str(count), str(hostname_or_ip)],
            capture_output=True, text=True
        ).stdout
        self.results = {}
        self.parse_data()

    def parse_data(self):
        for line in self.ping_data.split("\n"):
            if "icmp_seq=" in line:
                values = line.split(': ')[1].replace(" ms", "ms")  # quick and dirty
                self.results.update(dict(x.split("=") for x in values.split(" ")))
            elif "round-trip" in line:
                # round-trip min/avg/max/stddev = 37.762/37.762/37.762/0.000 ms
                values = line.split(" = ")[1].strip(" ms")
                ping_perf = values.split("/")
                self.results.update({'min': ping_perf[0],
                                     'avg': ping_perf[1],
                                     'max': ping_perf[2],
                                     'stddev': ping_perf[3]})
            elif "packet loss" in line:
                # 1 packets transmitted, 1 packets received, 0.0% packet loss
                y = [x.split(' ') for x in line.split(', ')]
                self.results.update({y[0][2]: y[0][0],
                                     y[1][2]: y[1][0],
                                     y[2][2]: y[2][0]
                                     })
