# coding:utf-8

from handler.hello import *

handlers = [(r"/api", IndexHandler),
            (r"/api/cart", CartHandler)]
