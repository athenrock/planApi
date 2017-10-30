# coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from data import mongodb
from data import boysDto
from tornado import gen
import json
from bson import json_util

from tornado.options import define, options


# define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        # obj =  {u'董效利': 29, u'武洪磊': 27, u'刘玉良': 30}
        boys = yield boysDto.find()
        # obj = [self.remove(boy) for boy in boys]
        # self.write(greeting + ', friendly user!')
        self.render("index.html", boys=boys)


class CartHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        obj = {u'董效利': 29, u'武洪磊': 27, u'刘玉良': 30}
        boys = yield boysDto.find()
        obj = [self.remove(boy) for boy in boys]
        self.write(dict(boys=obj))

    def remove(self, obj):
        del obj["_id"]
        return obj

    @gen.coroutine
    def post(self):
        surname = self.get_argument("surname")
        name = self.get_argument("name")
        sex = self.get_argument("sex")

        if not surname or not name or not sex:
            obj = dict(status=False, msg="参数缺失")
            self.write(obj)
            return

        boy = dict(surname=surname, name=name, sex=sex)
        i = yield boysDto.insert(**boy)
        obj = {
            "status": i > 0,
            "msg": ""
        }
        self.write(obj)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler), (r"/cart", CartHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print "http://localhost:8000"
    tornado.ioloop.IOLoop.instance().start()
