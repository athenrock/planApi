import mongodb

db = mongodb.get_db()

def find():
    table = db.boys
    return table.find()