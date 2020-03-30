from apps.resful import handler as user_handlers

url_patterns = [
    (r"", user_handlers.UserListHandler),
    (r"/(\d+)", user_handlers.UserHandler),
]
