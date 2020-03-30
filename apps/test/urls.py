# from apps.test.test import TestHandler
from .websocket_handler import WebsocketHandler
from .test import TestHandler, TestAsyncHandler

url_patterns = [
    (r"", TestHandler),
    (r"/Websocket", WebsocketHandler),
    (r"/TestAsync", TestAsyncHandler),
]
