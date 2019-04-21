import pymongo


class mongo_dao():
    def __init__(self, db):
        self.client = pymongo.MongoClient()
        self.db = self.client[db]
        self.collections = self.db.list_collection_names()
        self.guangdong = self.db['广东']
        result = self.guangdong.aggregate(
            [
                {"$group":
                    {
                        "_id":
                            {
                                "_id": "$_id",
                                # "city": "$city",
                                # "xiaoqu_name": "$xiaoqu_name",
                                # "position": "$position"
                            },
                        "count": {
                            "$avg": 1
                        }
                    }
                }
            ]
        )
        for i in result:
            print(i)
        # for collection in self.collections:

    # 总价最贵房子top10
    def total_price_house_max_top10(self):
        data = []

    # 总价最低房子top10
    def total_price_house_min_top10(self):
        data = []

    # 每平米最贵房子top10
    def unit_price_max_house_top10(self):
        data = []

    # 每平米最便宜房子top10
    def unit_price_min_house_top10(self):
        data = []

    # 总价最贵小区top10
    def total_price_max_xiaoqu_top10(self):
        data = []

    # 总价最低小区top10
    def total_price_min_xiaoqu_top10(self):
        data = []

    # 每平米最贵小区top10
    def unit_price_max_xiaoqu_top10(self):
        data = []

    # 每平米最便宜小区top10
    def unit_price_min_xiaoqu_top10(self):
        data = []

    # 每套房均价
    def total_price_house_average(self):
        data = []

    # 每平米均价
    def unit_price_house_average(self):
        data = []

    # 每个小区每套均价
    def total_price_xiaoqu_range(self):
        data = []

    # 每个小区每平米均价
    def unit_price_xiaoqu_range(self):
        data = []


if __name__ == '__main__':
    db = 'lianjia20190421'
    mongo = mongo_dao(db)
