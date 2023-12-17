class Colors:
    blue = '\x1b[38;5;39m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    green = '\u001b[32;226m'

    LIGHT_GREEN = "\033[1;32m"
    LIGHT_CYAN = "\033[1;36m"
    YELLOW = "\033[38;5;226m"
    LIGHT_RED = "\033[1;31m"
    BLINK = "\033[5m"
    END = "\033[0m"

    GREEN_BACKGROUND = "\033[1;97;42m"
    CYAN_BACKGROUND = "\033[1;97;46m"
    RED_BACKGROUND = "\033[1;97;41m"
    BROWN_BACKGROUND = "\033[1;97;43m"
    YELLOW_BACKGROUND = "\033[1;30;48;5;226m"
    RED_BACKGROUND_BLINK = "\033[1;97;5;41m"

    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32


if __name__ == '__main__':
    for i in dir(Colors):
        if i[0:1] != "_" and i != "END":
            print("{:>16} {}".format(i, getattr(Colors, i) + i + Colors.END))
