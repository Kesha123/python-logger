import logging
from python_logger.Logger import Logger

class ExampleClass:

    def __init__(self) -> None:
        self.logger = Logger( file="logs.log" )

    def foo(self, level) -> None:
        match level:
            case logging.DEBUG:
                self.logger.debug(f"example DEBUG")
            case logging.INFO:
                self.logger.info(f"example INFO")
            case logging.WARNING:
                self.logger.warning(f"example WARNING")
            case logging.ERROR:
                self.logger.error(f"example ERROR")
            case logging.CRITICAL:
                self.logger.critical(f"example CRITICAL")


example = ExampleClass()
example.foo(logging.DEBUG)
example.foo(logging.INFO)
example.foo(logging.WARNING)
example.foo(logging.ERROR)
example.foo(logging.CRITICAL)