import pymongo
import time
from data_visualize.gen_img import gen_charts
class mongo_dao():
    def __init__(self):
        self.price_range_map = {}
        for i in range(0, 100000, 10000):
            self.price_range_map['{}-{}'.format(i, i + 10000)] = {
                '$gte': i,
                '$lt': i + 10000
            }
        self.charts = gen_charts()
        self.client = pymongo.MongoClient()
        db = 'lianjia_newhouse' + str(time.strftime('%Y%m%d', time.localtime(time.time())))
        self.db = self.client[db]
        self.collections = self.db.list_collection_names()
        self.second_price_range(self.collections[0])

    def second_price_range(self, city_collection):
        city_collection = '深圳'
        collection = self.db[city_collection]
        range_key = []
        range_value = []
        for key, value in self.price_range_map.items():
            range_key.append(key)
            range_value.append(
                collection.find(
                    {
                        'huxing': {'$ne': ''},
                        'main_price': {'$ne': -1},
                        'second_price': {'$ne': -1},
                        'main_price': value
                    }
                ).count()
            )
        self.charts.pie_base(range_key,range_value,'{}市房价'.format(city_collection))
if __name__ == '__main__':
    mongo = mongo_dao()
