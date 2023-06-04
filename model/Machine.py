import json
import os
import platform
import sysconfig


class Machine:
    def __init__(self):
        self.os = os.name
        self.platform = sysconfig.get_platform()
        self.chip = platform.machine()
        self.chip_bits = platform.architecture()

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)


