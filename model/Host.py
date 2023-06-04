import json
import socket
import subprocess

from requests import get

from utilities.host_libs import is_valid_ipv4_address


class Host:
    def __init__(self):
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(socket.gethostname())
        self.host_gateway = self.get_default_ip()
        self.host_public_ip = self.get_external_ip()
        self.host_dns_servers = self.get_dns_ips()

    def get_default_ip(self, os='macos'):
        # TODO add code for OS specific calls
        if os == 'linux':
            output = subprocess.check_output(["ip", "-o", "route", "get", "1.1.1.1"],
                                             universal_newlines=True)
            return output.split(" ")[6]
        else:
            'route get default | grep gateway'
            ps = subprocess.Popen(('route', 'get', 'default'), stdout=subprocess.PIPE)
            output = subprocess.check_output(('grep', 'gateway'), stdin=ps.stdout, universal_newlines=True)
            ps.wait()
            return output.split(": ")[1]

    def get_external_ip(self):
        # TODO wrap in Try/Catch
        return get('https://api.ipify.org').content.decode('utf8')

    def get_dns_ips(self, os='macos'):
        dns_ips = []

        if os == 'macos':
            with open('/etc/resolv.conf') as fp:
                for cnt, line in enumerate(fp):
                    columns = line.split()
                    if columns[0] == 'nameserver':
                        ip = columns[1:][0]
                        if is_valid_ipv4_address(ip):
                            dns_ips.append(ip)
        elif os == 'Windows':
            output = subprocess.check_output(["ipconfig", "-all"])
            ipconfig_all_list = output.split('\n')

            for i in range(0, len(ipconfig_all_list)):
                if "DNS Servers" in ipconfig_all_list[i]:
                    # get the first dns server ip
                    first_ip = ipconfig_all_list[i].split(":")[1].strip()
                    if not is_valid_ipv4_address(first_ip):
                        continue
                    dns_ips.append(first_ip)
                    # get all other dns server ips if they exist
                    k = i + 1
                    while k < len(ipconfig_all_list) and ":" not in ipconfig_all_list[k]:
                        ip = ipconfig_all_list[k].strip()
                        if is_valid_ipv4_address(ip):
                            dns_ips.append(ip)
                        k += 1
                    # at this point we're done
                    break

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
