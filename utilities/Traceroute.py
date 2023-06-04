import subprocess
import re
from collections import namedtuple

Station = namedtuple('Station', ['ip', 'latency_ms'])


class Traceroute:
    def __init__(self, hostname_or_ip: str):
        self.traceroute_data = subprocess.run(
            ["traceroute", "-4", "-N1", "-n", hostname_or_ip],
            capture_output=True
        ).stdout.decode()
        self.route_list = []

        self.parse_data()

    def parse_data(self):
        station_regex = r"(?P<station_number>\d+)  (?P<ip_address>\d+\.\d+\.\d+\.\d+)  (?P<latency>\d+\.\d+) ms"

        for line in self.traceroute_data.split("\n"):
            re_match = re.search(station_regex, line)

            if re_match:
                ip_address = re_match.group("ip_address")
                latency = float(re_match.group("latency"))

                self.route_list.append(Station(ip_address, latency))
            elif '*' in line:
                self.route_list.append(Station('*', '*'))
