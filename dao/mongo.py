import pymongo


class mongo_dao():
    def __init__(self, db):
        self.client = pymongo.MongoClient()
        self.db = self.client[db]
        self.city = '广州'
        self.coll = self.db[self.city]
        self.collection = self.db.list_collection_names()
        self.aggs = [
            {"$match": {
                "$and": [
                    {
                        "unit_price": {
                            "$gte": 10000,
                            "$lte": 50000
                        }
                    },
                    {
                        "city": self.city
                    }
                ]
            }
            },
            {"$group":
                {
                    "_id":
                        {
                            "_id":"$_id",
                            "city": "$city",
                            "xiaoqu_name": "$xiaoqu_name",
                            "position": "$position"
                        },
                    # "title": "$title",
                    # "unit_price": "$unit_price",
                    # "total_price": "$total_price",
                    "count": {
                        "$sum": 1
                    }
                }
            },
        ]
        result = self.coll.aggregate(self.aggs)
        for i in result:
            print(i)


if __name__ == '__main__':
    db = 'lianjia20190421'
    mongo = mongo_dao(db)
