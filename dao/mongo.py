import pymongo
import time


class mongo_dao():
    def __init__(self):
        self.client = pymongo.MongoClient()
        db = 'lianjia_newhouse' + str(time.strftime('%Y%m%d', time.localtime(time.time())))
        self.db = self.client[db]
        self.collections = self.db.list_collection_names()
        for collection in self.collections:
            self.parse_data(collection)

    def parse_data(self, city_collection):
        collection = self.db[city_collection]
        data = collection.find_one(
            {
                '$and':[
                    {
                        'main_price':{
                            '$gte':1000,
                            '$lt':10000
                        }
                    }
                ]
            }
        )
        print(data)
        exit(0)

if __name__ == '__main__':
    mongo = mongo_dao()
