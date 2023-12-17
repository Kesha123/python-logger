import logging
from python_logger.Colors import Colors

class Formatter(logging.Formatter):

    def __init__(
            self,
            fmt,
            colored_message = True,
            warning_yellow = False
        ):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG:
                Colors.GREEN_BACKGROUND + "DEBUG" + Colors.END + " " +
                (
                    Colors.green + self.fmt + Colors.END if colored_message
                    else self.fmt
                ),

            logging.INFO:
                Colors.CYAN_BACKGROUND  + "INFO" + Colors.END + " " +
                (
                    Colors.blue + self.fmt + Colors.END if colored_message
                    else self.fmt
                ),

            logging.WARNING:
                (Colors.YELLOW_BACKGROUND if warning_yellow else Colors.BROWN_BACKGROUND) +
                "WARNING" + Colors.END + " " +
                (
                    Colors.YELLOW + self.fmt + Colors.END if colored_message
                    else self.fmt
                ),

            logging.ERROR:
                Colors.RED_BACKGROUND  + "ERROR" + Colors.END + " " +
                (
                    Colors.red + self.fmt + Colors.END if colored_message
                    else self.fmt
                ),

            logging.CRITICAL:
                Colors.RED_BACKGROUND_BLINK + "CRITICAL"
                + Colors.END + " " + self.fmt,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
