import pymongo
import time
from data_visualize.echarts import charts
import os
from data_visualize.common import *
from pyecharts.render import make_snapshot
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot

# 新房数据分析
class newhouse_dao():
    def __init__(self):
        self.path = base_path + "\\newhouse"
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.charts = charts()
        self.client = pymongo.MongoClient()
        db = 'lianjia_newhouse' + str(time.strftime('%Y%m%d', time.localtime(time.time())))
        self.db = self.client[db]
        self.collections = self.db.list_collection_names()
        for city in self.collections:
            self.main_price_range(city)
            self.second_price_range(city)

    # 每平米价位占比
    def main_price_range(self, city):
        match = get_main_price_range(city)
        save_dir = self.path + "\\main_price_range"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        collection = self.db[city]
        range_key = []
        range_value = []
        if match:
            for key, value in match.items():
                range_key.append(key)
                range_value.append(
                    collection.find(
                        {
                            'huxing': {'$ne': ''},
                            'main_price': {'$ne': -1},
                            'second_price': {'$ne': -1},
                            'main_price': value,
                            'main_price_desc': '元/平(均价)'
                        }
                    ).count()
                )
        bar = self.charts.bar(range_key, range_value, city,
                              main_price_range_template.format(city), "单位: 元/m²")
        make_snapshot(snapshot, bar.render(), "{}\\{}.gif".format(save_dir, main_price_range_template.format(city)))
        print("finished {}  main_price_range".format(city))

    # 每套房各价位占比
    def second_price_range(self, city):
        match = get_second_price_range(city)
        range_key = []
        range_value = []
        save_dir = self.path + "\\second_price_range"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        collection = self.db[city]
        if match:
            for key, value in match.items():
                range_key.append(key + "万")
                range_value.append(
                    collection.find(
                        {
                            'huxing': {'$ne': ''},
                            'second_price': {'$ne': -1},
                            'second_price': value,
                        }
                    ).count()
                )
        bar = self.charts.pie(range_key, range_value, second_price_range_template.format(city))
        make_snapshot(snapshot, bar.render(), "{}\\{}.gif".format(save_dir, second_price_range_template.format(city)))
        print("finished {}  second_price_range".format(city))


if __name__ == '__main__':
    mongo = newhouse_dao()
