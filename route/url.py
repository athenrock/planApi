# coding:utf-8

from handler.hello import *

handlers = [(r"/", IndexHandler),
            (r"/cart", CartHandler)]
