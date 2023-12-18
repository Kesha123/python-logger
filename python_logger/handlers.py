import datetime
from dataclasses import dataclass, field


@dataclass
class JSONHandlerFormat:
    timestamp: str = field( default_factory = lambda: datetime.datetime.today().isoformat() )
    level: int = field( default_factory = lambda: None )
    message: str = field( default_factory = lambda: None )


@dataclass
class FileHandler:
    file: int = field( default_factory = lambda: 'logs.log' )
    level: int = field( default_factory = lambda: None )


@dataclass
class StreamHandler:
    level: int = field( default_factory = lambda: None )


@dataclass
class HandlerLevel:
    stream: StreamHandler = field( default_factory = lambda: None )
    file: FileHandler = field( default_factory = lambda: None )
