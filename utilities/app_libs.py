import json
from typing import Any

from utilities.Lumberjack import Lumberjack


logout = Lumberjack(__name__)


def read_conf(file_path):
    res: dict[Any, Any] = {}
    try:
        with open(file_path, 'r') as read_content:
            res = json.load(read_content)
    except TypeError:
        logout.logger.error('Cannot read file: {}'.format(file_path))
    except ImportError:
        logout.logger.error('Cannot read file: {}'.format(file_path))

    return res
