import cx_Oracle
from .base import DbBase


class DbOracle(DbBase):

    def __init__(self, user, password, name, host, port):
        super().__init__()
        self.user = user
        self.password = password
        self.name = name
        self.host = host
        self.port = port

    def connect(self):
        self.db = cx_Oracle.connect(
            self.user,
            self.password,
            f"{self.host}:{self.port}/{self.name}"
        )
        self.cursor = self.db.cursor()
