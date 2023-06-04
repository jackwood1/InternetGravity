import uuid
import time

from model.Machine import Machine
from model.Host import Host
from utilities.Lumberjack import Lumberjack
from utilities.Traceroute import Traceroute
from utilities.Ping import Ping
from utilities.app_libs import read_conf


def app(mode):
    if mode == 'run':
        my_machine = Machine()
        my_host = Host()
        host_data = {
            'version': 1.0,
            'time': time.time(),
            'uuid': str(uuid.uuid4()),
            'platform': my_machine.toJson(),
            'host_info': my_host.toJson()
        }
        ping = Ping(CONFIG['NETWORK']['PIMG_HOSTS'][0], CONFIG['NETWORK']['COUNT'])
        tr = Traceroute(CONFIG['NETWORK']['PIMG_HOSTS'][0])
        logout.logger.info(tr.route_list)
        logout.logger.info(ping.results)
        logout.logger.info(host_data)
    elif mode == 'test':
        logout.logger.debug('Testing, one two three')


if __name__ == '__main__':
    logout = Lumberjack(__name__)
    logout.logger.info('Starting the application')
    CONFIG = read_conf('../config/config.json')
    app(CONFIG['APP']['ENVIRONMENT'])
    logout.logger.info('Finished running')
