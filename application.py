# coding:utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web

from config.config import *
from tornado.options import define, options
from route import url, api


define("port", default=8000, help="run on th given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        admin = url.handlers.append(api.handlers)
        super(Application, self).__init__(admin, **setting)



def main():
    # 读取server的配置文件。
    # conf_server=ServerConfig.get("")
    # options.port=int(conf_server.getPort())

    tornado.options.parse_command_line()
    app = tornado.web.Application(Application(), xheaders=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:8000/')
    print('Quit the server with Control-C')
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print ("exit")


if __name__ == "__main__" or 1 == 1:
    main()
