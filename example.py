import logging
from python_logger.Logger import Logger

class ExampleClass:

    def __init__(self) -> None:
        self.logger = Logger( file="logs.log" )

    def foo(self, level) -> None:
        match level:
            case logging.DEBUG:
                self.logger.debug("example DEBUG")
            case logging.INFO:
                self.logger.info("example INFO")
            case logging.WARNING:
                self.logger.warning("example WARNING")
            case logging.ERROR:
                self.logger.error("example ERROR")
            case logging.CRITICAL:
                self.logger.critical("example CRITICAL")


example = ExampleClass()
example.foo(logging.DEBUG)
example.foo(logging.INFO)
example.foo(logging.WARNING)
example.foo(logging.ERROR)
example.foo(logging.CRITICAL)