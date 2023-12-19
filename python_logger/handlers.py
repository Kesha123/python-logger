import logging
import datetime
from logging import LogRecord
from pymongo import MongoClient
from dataclasses import dataclass, field


@dataclass
class JSONHandlerFormat:
    timestamp: str = field( default_factory = lambda: datetime.datetime.today().isoformat() )
    level: int = field( default_factory = lambda: logging.DEBUG )
    message: str = field( default_factory = lambda: None )


@dataclass
class FileHandler:
    file: int = field( default_factory = lambda: 'logs.log' )
    level: int = field( default_factory = lambda: logging.DEBUG )


@dataclass
class StreamHandler:
    level: int = field( default_factory = lambda: logging.DEBUG )


class MongoDBHandler(logging.Handler):

    def __init__(self, level: int, connection_string: str, database: str, collection: str) -> None:
        super().__init__(level)
        self.__connection_string = connection_string
        self.__database = database
        self.__collection = collection
        self.__connection = self.__init_connection()

    def __init_connection(self):
        self.mongodb_client = MongoClient(self.__connection_string)
        return self.mongodb_client[self.__database][self.__collection]

    def emit(self, record: LogRecord) -> None:
        if record.levelno >= self.level:
            self.__connection.insert_one({
                "timestamp": datetime.datetime.today().isoformat(),
                "level": record.levelname,
                "messsage": record.getMessage()
            })


@dataclass
class HandlerLevel:
    stream: StreamHandler = field( default_factory = lambda: None )
    file: FileHandler = field( default_factory = lambda: None )
    mongodb: MongoDBHandler = field( default_factory = lambda: None )
