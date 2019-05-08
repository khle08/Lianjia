import pymongo
import time
client = pymongo.MongoClient()
db = 'lianjia_ershoufang' + str(time.strftime('%Y%m%d', time.localtime(time.time())))
db = client[db]
collections = db.list_collection_names()
print(collections)