import os
import logging
import datetime
from python_logger.Formatter import CustomFormatter as Formatter


class Logger:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    fmt = '%(asctime)s | %(message)s'

    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(Formatter(fmt))

    today = datetime.date.today()
    file_handler = logging.FileHandler(os.getenv('FILE_HANDLER_PATH').format(today.strftime('%Y_%m_%d')))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(fmt))

    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    @staticmethod
    def debug(message):
        Logger.logger.debug(message)

    @staticmethod
    def info(message):
        Logger.logger.info(message)

    @staticmethod
    def warning(message):
        Logger.logger.warning(message)

    @staticmethod
    def error(message):
        Logger.logger.error(message)

    @staticmethod
    def critical(message):
        Logger.logger.critical(message)