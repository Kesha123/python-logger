import os
import logging
import datetime
from python_logger.Formatter import Formatter

class Logger:
    _instance = None

    def __new__(cls, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(
            self,
            file: str = "./logs.log",
            level = logging.DEBUG,
            **kwargs
        ):
        if not self.__initialized:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(level)

            fmt = '%(asctime)s | %(message)s'

            stdout_handler = logging.StreamHandler()
            stdout_handler.setLevel(level)
            formatter = Formatter(fmt, **kwargs)
            stdout_handler.setFormatter(formatter)

            today = datetime.date.today()
            file_handler = logging.FileHandler((file).format(today.strftime('%Y_%m_%d')))
            file_handler.setLevel(level)
            file_handler.setFormatter(logging.Formatter(fmt))

            self.logger.addHandler(stdout_handler)
            self.logger.addHandler(file_handler)

            self.__initialized = True

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
