from abc import ABC
from apps.base.base_handler import BaseWebsocketHandler


class WebsocketHandler(BaseWebsocketHandler, ABC):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")


