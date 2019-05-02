import pymongo
import time
from data_visualize.echarts import charts
import os
from data_visualize.common import *
from pyecharts.render import make_snapshot
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot


class ershoufang_dao():
    unit_price_template = '{}市二手房每平米楼盘价位占比分布图'
    total_price_template = '{}市'

    def __init__(self):
        self.path = base_path + "\\ershoufang"
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.charts = charts()
        self.client = pymongo.MongoClient()
        db = 'lianjia_ershoufang' + str(time.strftime('%Y%m%d', time.localtime(time.time())))
        self.db = self.client[db]
        self.collections = self.db.list_collection_names()
        # 每平米均价
        self.avg_price_square_meter = []
        # 每套房均价
        self.avg_loupan = []
        for city in self.collections:
            self.main_price_range(city)
            self.second_price_range(city)
        # self.avg_square_meter(self.collections)
        # self.avg_loupan_price(self.collections)

    # 每平米价位占比
    def main_price_range(self, city):
        match = get_main_price_range(city)
        save_dir = self.path + "\\unit_price_range"
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
                            'unit_price': {'$ne': -1},
                            'total_price': {'$ne': -1},
                            'unit_price': value,
                        }
                    ).count()
                )
        bar = self.charts.bar(range_key, range_value, city,
                             self.unit_price_template.format(city), "单位: 元/m²")
        make_snapshot(snapshot, bar.render(), "{}\\{}.gif".format(save_dir, self.unit_price_template.format(city)))
        print("finished {}  unit_price_range".format(city))

    # 每套房各价位占比
    def second_price_range(self, city):
        match = get_second_price_range(city)
        range_key = []
        range_value = []
        save_dir = self.path + "\\total_price_range"
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
                            'total_price': {'$ne': -1},
                            'total_price': value,
                        }
                    ).count()
                )
        bar = self.charts.pie(range_key, range_value, self.total_price_template.format(city))
        make_snapshot(snapshot, bar.render(), "{}\\{}.gif".format(save_dir, self.total_price_template.format(city)))
        print("finished {}  total_price_range".format(city))

    # 每平米均价
    def avg_square_meter(self, collections):
        save_dir = self.path + "\\avg_square_meter"
        first_key = []
        new_first_key = []
        second_key = []
        third_key = []
        forth_key = []
        fifth_key = []
        first_value = []
        new_first_value = []
        second_value = []
        third_value = []
        forth_value = []
        fifth_value = []
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        for city in collections:
            average_price = list(self.db[city].aggregate(
                [
                    {
                        '$match': {
                            'unit_price': {
                                '$ne': -1
                            }
                        }
                    },
                    {
                        '$group': {
                            '_id': 'city',
                            'unit_price_avg': {
                                '$avg': '$unit_price'
                            }
                        }
                    }
                ]
            ))
            dict = {}
            if average_price:
                dict[city] = int(average_price[0]['unit_price_avg'])
                if city in lianjia_ershoufang_citys['first']:
                    first_key.append(city)
                    first_value.append(int(average_price[0]['unit_price_avg']))
                if city in lianjia_ershoufang_citys['new_first']:
                    new_first_key.append(city)
                    new_first_value.append(int(average_price[0]['unit_price_avg']))
                if city in lianjia_ershoufang_citys['second']:

            self.avg_price_square_meter.append(dict)
        first_bar = self.charts.bar(first_key, first_value, "",
                                    first_level_avg_square_template, temproary_loss)
        make_snapshot(snapshot, first_bar.render(), "{}\\{}.gif".format(save_dir, first_level_avg_square_template))
        second_land_bar = self.charts.bar(second_land_key, second_land_value, "",
                                          second_level_land_avg_square_template, temproary_loss)
        make_snapshot(snapshot, second_land_bar.render(), "{}\\{}.gif".format(save_dir,
                                                                              second_level_land_avg_square_template))
        second_sea_bar = self.charts.bar(second_sea_key, second_sea_value, "",
                                         second_level_sea_avg_square_template, temproary_loss)
        make_snapshot(snapshot, second_sea_bar.render(), "{}\\{}.gif".format(save_dir,
                                                                             second_level_sea_avg_square_template))
        third_bar = self.charts.bar(third_key, third_value, "",
                                    third_level_avg_square_template, temproary_loss)
        make_snapshot(snapshot, third_bar.render(), "{}\\{}.gif".format(save_dir, third_level_avg_square_template))
        forth_bar = self.charts.bar(forth_key, forth_value, "",
                                    forth_level_avg_square_template, temproary_loss)
        make_snapshot(snapshot, forth_bar.render(), "{}\\{}.gif".format(save_dir, forth_level_avg_square_template))
        fifth_bar = self.charts.bar(fifth_key, fifth_value, "",
                                    fifth_level_avg_square_template, temproary_loss)
        make_snapshot(snapshot, fifth_bar.render(), "{}\\{}.gif".format(save_dir, fifth_level_avg_square_template))
        print("finish count avg square meter price")

    # 每套房均价
    def avg_loupan_price(self, collections):
        save_dir = self.path + "\\avg_loupan"
        first_key = []
        second_land_key = []
        second_sea_key = []
        third_key = []
        forth_key = []
        fifth_key = []
        first_value = []
        second_land_value = []
        second_sea_value = []
        third_value = []
        forth_value = []
        fifth_value = []
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        for city in collections:
            average_price = list(self.db[city].aggregate(
                [
                    {
                        '$match': {
                            'total_price': {
                                '$ne': -1
                            }
                        }
                    },
                    {
                        '$group': {
                            '_id': 'city',
                            'total_price_avg': {
                                '$avg': '$total_price'
                            }
                        }
                    }
                ]
            ))
            dict = {}
            if average_price:
                dict[city] = int(average_price[0]['total_price_avg'])
                if city in first_level:
                    first_key.append(city)
                    first_value.append(int(average_price[0]['total_price_avg']))
                if city in second_land_level:
                    second_land_key.append(city)
                    second_land_value.append(int(average_price[0]['total_price_avg']))
                if city in second_near_sea_level:
                    second_sea_key.append(city)
                    second_sea_value.append(int(average_price[0]['total_price_avg']))
                if city in third_level:
                    third_key.append(city)
                    third_value.append(int(average_price[0]['total_price_avg']))
                if city in forth_level:
                    forth_key.append(city)
                    forth_value.append(int(average_price[0]['total_price_avg']))
                if city in fifth_level:
                    fifth_key.append(city)
                    fifth_value.append(int(average_price[0]['total_price_avg']))
            self.avg_loupan.append(dict)
        first_bar = self.charts.bar(first_key, first_value, "",
                                    first_level_avg_loupan, temproary_loss)
        make_snapshot(snapshot, first_bar.render(), "{}\\{}.gif".format(save_dir, first_level_avg_loupan))
        second_land_bar = self.charts.bar(second_land_key, second_land_value, "",
                                          second_level_land_avg_loupan, temproary_loss)
        make_snapshot(snapshot, second_land_bar.render(), "{}\\{}.gif".format(save_dir,
                                                                              second_level_land_avg_loupan))
        second_sea_bar = self.charts.bar(second_sea_key, second_sea_value, "",
                                         second_level_sea_avg_loupan, temproary_loss)
        make_snapshot(snapshot, second_sea_bar.render(), "{}\\{}.gif".format(save_dir,
                                                                             second_level_sea_avg_loupan))
        third_bar = self.charts.bar(third_key, third_value, "",
                                    third_level_avg_loupan, temproary_loss)
        make_snapshot(snapshot, third_bar.render(), "{}\\{}.gif".format(save_dir, third_level_avg_loupan))
        forth_bar = self.charts.bar(forth_key, forth_value, "",
                                    forth_level_avg_loupan, temproary_loss)
        make_snapshot(snapshot, forth_bar.render(), "{}\\{}.gif".format(save_dir, forth_level_avg_loupan))
        fifth_bar = self.charts.bar(fifth_key, fifth_value, "",
                                    fifth_level_avg_loupan, temproary_loss)
        make_snapshot(snapshot, fifth_bar.render(), "{}\\{}.gif".format(save_dir, fifth_level_avg_loupan))
        print("finish count avg loupan price")


if __name__ == '__main__':
    ershoufang = ershoufang_dao()
