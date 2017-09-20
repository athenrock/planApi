from tornado import gen

import mongodb

db = mongodb.get_db()
table = db.boys


@gen.coroutine
def find():
    boys = table.find()
    raise gen.Return(boys)


@gen.coroutine
def insert(**kwarg):
    i = table.insert(kwarg)
    raise gen.Return(i)
