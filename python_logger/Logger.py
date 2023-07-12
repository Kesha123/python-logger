import os
import logging
import datetime
from python_logger.Formatter import CustomFormatter as Formatter

class Logger:

    def __init__(self, **kwargs) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        fmt = '%(asctime)s | %(message)s'

        self.class_name = kwargs.get("class_name")

        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(Formatter(fmt))

        today = datetime.date.today()
        file_handler = logging.FileHandler((kwargs.get("file") if kwargs.get("file") else "./logs.log").format(today.strftime('%Y_%m_%d')))
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(fmt))

        self.logger.addHandler(stdout_handler)
        self.logger.addHandler(file_handler)

    def debug(self, message):
        message = f"{self.class_name} | {message}"
        self.logger.debug(message)

    def info(self, message):
        message = f"{self.class_name} | {message}"
        self.logger.info(message)

    def warning(self, message):
        message = f"{self.class_name} | {message}"
        self.logger.warning(message)

    def error(self, message):
        message = f"{self.class_name} | {message}"
        self.logger.error(message)

    def critical(self, message):
        message = f"{self.class_name} | {message}"
        self.logger.critical(message)
