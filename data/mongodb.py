# coding:utf-8

from pymongo import MongoClient

#建立MongoDB数据库连接
client = MongoClient('localhost',27017)

#连接所需数据库,test为数据库名
#db=client.test
def get_db():
    db = client.demo
    return db


if __name__=="__main__":
    db = get_db()
    boys = db.boys

    #boys.insert({'name':"效利",'sex':1})

    #boys.update({'name':"效利"},{'name':"效利",'surname':'董','sex':1})
    #boys.insert({'name': "洪磊", 'surname':'武', 'sex': 1})
    boys.insert({'name': "玉良", 'surname': '刘', 'sex': 1})
    boys.insert({'name': "辉", 'surname': '王', 'sex': 1})
    boys.insert({'name': "冰洁", 'surname': '张', 'sex': 2})
    boys.insert({'name': "玉", 'surname': '袁', 'sex': 2})

    for boy in boys.find():
        print boy


#连接所用集合，也就是我们通常所说的表，test为表名
#collection=db.test

#接下里就可以用collection来完成对数据库表的一些操作

#查找集合中所有数据
#for item in collection.find():
#    print item

#查找集合中单条数据
#print collection.find_one()

#向集合中插入数据
#collection.insert({'name':'Tom','age':25,'addr':'Cleveland'})

#更新集合中的数据,第一个大括号里为更新条件，第二个大括号为更新之后的内容
#collection.update({'Name':'Tom'},{'Name':'Tom','age':18})

#删除集合collection中的所有数据
#collection.remove()

#删除集合collection
#collection.drop()