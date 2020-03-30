from abc import ABC

import tornado.web
from tornado.escape import json_encode


class TestHandler(tornado.web.RequestHandler, ABC):

    def get(self):
        sql = "SELECT * FROM USERS_ROLE"

        result = self.application.db.get_all(sql)

        print("testing!")

        self.write(json_encode("Hello world."))


class TestAsyncHandler(tornado.web.RequestHandler, ABC):

    def get(self):

        print("testing!")

        self.write(json_encode("Hello world."))
