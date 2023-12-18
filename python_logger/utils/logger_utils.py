from python_logger.handlers import HandlerLevel


def highest_level(handler_level: HandlerLevel) -> int:
    levels = []
    if handler_level.stream:
        levels.append(handler_level.stream.level)
    if handler_level.file:
        levels.append(handler_level.file.level)
    return min(levels)