# coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from data import mongodb
from data import boysDto
import json
from bson import json_util

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

class CartHandler(tornado.web.RequestHandler):
    def get(self):
        # title = self.get_argument('title')
        # if(title == "three2B"):
        obj ={u'董效利':29, u'武洪磊':27, u'刘玉良':30}
        # elif(title == "threeboy"):
        #     obj = {u'董效利': 29, u'武洪磊': 27, u'刘玉良': 30, u'张冰洁': 27}
        # else:
        #     obj ={u'王辉':35}
        #
        boys = boysDto.find()
        print type(boys)
        for boy in boys:
            del boy["_id"]

        obj = json.dumps(boys)
        #abc = next(boys, None)
        #obj = json.dumps(boys)
        #for boy in boys:
        #
        #     print boy.get("surname"), boy.get("name")

        self.write(obj)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler),(r"/cart", CartHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print "http://localhost:8000"
    tornado.ioloop.IOLoop.instance().start()
