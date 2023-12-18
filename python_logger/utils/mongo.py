import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class MongoConnection:
    instance = None

    __connection = None

    def __new__(cls, connection_string: str, database: str):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, connection_string: str, database: str ) -> None:
        if (self.__connection is None) or self.__is_closed():
            self.__connect(connection_string, database)

    def __connect(self, connection_string: str, database: str):
        self.mongodb_client = MongoClient(connection_string)
        self.__connection = self.mongodb_client[database]

    def __is_closed(self):
        try:
            self.mongodb_client.admin.command("ismaster")
            return True
        except ConnectionFailure:
            return False

    def get_connection(self):
        return self.__connection