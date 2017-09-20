# coding:utf-8
import os
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
import sys
from config.config import *
from handler import *

from tornado.options import define, options

from handler.hello import IndexHandler, CartHandler

define("port", default=8000, help="run on th given port", type=int)

handlers = [(r"/", IndexHandler), (r"/cart", CartHandler)]
setting = dict(
    template_path=os.path.join(os.path.dirname(__file__), "views"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)


#
# if __name__ == "__main__":
#     tornado.options.parse_command_line()
#     app = tornado.web.Application(handlers=[(r"/", IndexHandler), (r"/cart", CartHandler)])
#     http_server = tornado.httpserver.HTTPServer(app)
#     http_server.listen(options.port)
#     print "http://localhost:8000"
#     tornado.ioloop.IOLoop.instance().start()

def main():
    # 读取server的配置文件。
    # conf_server=ServerConfig.get("")
    # options.port=int(conf_server.getPort())

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers, **setting)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:8000/')
    print('Quit the server with Control-C')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__" or 1 == 1:
    main()
