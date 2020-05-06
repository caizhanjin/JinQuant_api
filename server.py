import tornado.ioloop
import tornado.web
import tornado.httpserver
import sys
import settings

from urls import urls_patterns as url_handlers
from tornado.options import options
# from sqlalchemy.orm import scoped_session, sessionmaker


class Application(tornado.web.Application):
    def __init__(self, handlers, **setting):
        tornado.web.Application.__init__(self, handlers, **setting)
        self.db = settings.ORACLE_ENGINE
        # self.db_orm = scoped_session(sessionmaker(
        #     bind=settings.ORM_ENGINE,
        #     autocommit=False, autoflush=True,
        #     expire_on_commit=False
        # ))


application = Application(url_handlers, **settings.settings)


def main():
    try:
        print(f"Starting server at: {'http://' + options.host + ':' + str(options.port)}")
        options.parse_command_line()
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("Server got to stop.")
    except:
        import traceback
        print(traceback.print_exc())
    finally:
        sys.exit(0)


if __name__ == "__main__":
    main()
