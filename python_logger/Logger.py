import os
import logging
import datetime
from python_logger.handlers import *
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
            handlers: HandlerLevel = HandlerLevel(
                stream = StreamHandler(level = logging.DEBUG),
                file = FileHandler(level = logging.DEBUG)
            ),
            **kwargs
        ):
        if not self.__initialized:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel( min(handlers.stream.level, handlers.file.level) )

            fmt = '%(asctime)s | %(message)s'

            if handlers.stream:
                stdout_handler = logging.StreamHandler()
                stdout_handler.setLevel(handlers.stream.level)
                formatter = Formatter(fmt, **kwargs)
                stdout_handler.setFormatter(formatter)
                self.logger.addHandler(stdout_handler)

            if handlers.file:
                today = datetime.date.today()
                file_handler = logging.FileHandler((handlers.file.file).format(today.strftime('%Y_%m_%d')))
                file_handler.setLevel(handlers.file.level)
                file_handler.setFormatter(logging.Formatter(fmt))
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
