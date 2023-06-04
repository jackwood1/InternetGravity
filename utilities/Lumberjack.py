import logging


class Lumberjack:
    def __init__(self, name) -> object:
        file_formatter = logging.Formatter(
            '%(asctime)s~%(levelname)s~%(message)s~module:%(module)s~function:%(module)s')
        file_handler = logging.FileHandler("../logs/logfile.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(file_formatter)

        console_formatter = logging.Formatter('%(levelname)s -- %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(console_formatter)

        self.logger = logging.getLogger(name)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        self.logger.setLevel(logging.DEBUG)
        