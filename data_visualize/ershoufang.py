import pymongo
import time
from data_visualize.echarts import charts
import os
from data_visualize.common import *
from pyecharts.render import make_snapshot
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot


class ershoufang():
    unit_price_template = '{}市二手房每平米楼盘价位占比分布图'
    total_price_template = '{}市二手房每套房价位占比分布图'
    yuan_per_square = '元/平'
    ten_thousand_per_loupan = '万/套'
    square_price_max_top5 = '{}市二手房每平米最贵top5小区'
    square_price_min_top5 = '{}市二手房每平米最便宜top5小区'

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
            self.unit_price_range(city)
            self.total_price_range(city)
        self.avg_square_meter(self.collections)
        self.avg_loupan_price(self.collections)
        self.square_meter_max_top5(self.collections)
        self.square_meter_min_top5(self.collections)
        self.xiaoqu_wordcloud(self.collections)
        self.position_wordcloud(self.collections)

    # 每平米价位占比
    def unit_price_range(self, city):
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
        print("完成二手房每平米价位占比作图".format(city))

    # 每套房各价位占比
    def total_price_range(self, city):
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
        bar = self.charts.pie_radius(range_key, range_value, self.total_price_template.format(city))
        make_snapshot(snapshot, bar.render(), "{}\\{}.gif".format(save_dir, self.total_price_template.format(city)))
        print("完成二手房每套房价位占比作图".format(city))

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
                if city in lianjia_citys['first']:
                    first_key.append(city)
                    first_value.append(int(average_price[0]['unit_price_avg']))
                if city in lianjia_citys['new_first']:
                    new_first_key.append(city)
                    new_first_value.append(int(average_price[0]['unit_price_avg']))
                if city in lianjia_citys['second']:
                    second_key.append(city)
                    second_value.append(int(average_price[0]['unit_price_avg']))
                if city in lianjia_citys['third']:
                    third_key.append(city)
                    third_value.append(int(average_price[0]['unit_price_avg']))
                if city in lianjia_citys['forth']:
                    forth_key.append(city)
                    forth_value.append(int(average_price[0]['unit_price_avg']))
                if city in lianjia_citys['fifth']:
                    fifth_key.append(city)
                    fifth_value.append(int(average_price[0]['unit_price_avg']))
            self.avg_price_square_meter.append(dict)
        first_bar = self.charts.bar(first_key, first_value, "", '一线城市二手房每平米均价', self.yuan_per_square)
        make_snapshot(snapshot, first_bar.render(), "{}\\{}.gif".format(save_dir, '一线城市二手房每平米均价', ))
        new_first_bar = self.charts.bar(new_first_key[:10], new_first_value[:10], "",
                                        '新一线城市二手房每平米均价(1)', self.yuan_per_square)
        make_snapshot(snapshot, new_first_bar.render(), "{}\\{}.gif".format(save_dir, '新一线城市二手房每平米均价(1)', ))
        new_first_bar2 = self.charts.bar(new_first_key[10:], new_first_value[10:], "",
                                         '新一线城市二手房每平米均价(2)', self.yuan_per_square)
        make_snapshot(snapshot, new_first_bar2.render(), "{}\\{}.gif".format(save_dir, '新一线城市二手房每平米均价(2)', ))
        second_bar = self.charts.bar(second_key[:10], second_value[:10], "",
                                     '二线城市二手房每平米均价(1)', self.yuan_per_square)
        make_snapshot(snapshot, second_bar.render(), "{}\\{}.gif".format(save_dir,
                                                                         '二线城市二手房每平米均价(1)'))
        second_bar2 = self.charts.bar(second_key[10:20], second_value[10:20], "",
                                      '二线城市二手房每平米均价(2)', self.yuan_per_square)
        make_snapshot(snapshot, second_bar2.render(), "{}\\{}.gif".format(save_dir,
                                                                          '二线城市二手房每平米均价(2)'))
        second_bar3 = self.charts.bar(second_key[20:], second_value[20:], "",
                                      '二线城市二手房每平米均价(3)', self.yuan_per_square)
        make_snapshot(snapshot, second_bar3.render(), "{}\\{}.gif".format(save_dir,
                                                                          '二线城市二手房每平米均价(3)'))
        third_bar = self.charts.bar(third_key[:10], third_value[:10], "",
                                    '三线城市二手房每平米均价(1)', self.yuan_per_square)
        make_snapshot(snapshot, third_bar.render(), "{}\\{}.gif".format(save_dir, '三线城市二手房每平米均价(1)'))
        third_bar2 = self.charts.bar(third_key[10:20], third_value[10:20], "",
                                     '三线城市二手房每平米均价(2)', self.yuan_per_square)
        make_snapshot(snapshot, third_bar2.render(), "{}\\{}.gif".format(save_dir, '三线城市二手房每平米均价(2)'))
        third_bar3 = self.charts.bar(third_key[20:], third_value[20:], "",
                                     '三线城市二手房每平米均价(3)', self.yuan_per_square)
        make_snapshot(snapshot, third_bar3.render(), "{}\\{}.gif".format(save_dir, '三线城市二手房每平米均价(3)'))
        forth_bar = self.charts.bar(forth_key[:10], forth_value[:10], "",
                                    '四线城市二手房每平米均价(1)', self.yuan_per_square)
        make_snapshot(snapshot, forth_bar.render(), "{}\\{}.gif".format(save_dir, '四线城市二手房每平米均价(1)'))
        forth_bar2 = self.charts.bar(forth_key[10:20], forth_value[10:20], "",
                                     '四线城市二手房每平米均价(2)', self.yuan_per_square)
        make_snapshot(snapshot, forth_bar2.render(), "{}\\{}.gif".format(save_dir, '四线城市二手房每平米均价(2)'))
        forth_bar3 = self.charts.bar(forth_key[20:], forth_value[20:], "",
                                     '四线城市二手房每平米均价(3)', self.yuan_per_square)
        make_snapshot(snapshot, forth_bar3.render(), "{}\\{}.gif".format(save_dir, '四线城市二手房每平米均价(3)'))
        fifth_bar = self.charts.bar(fifth_key, fifth_value, "",
                                    '五线城市二手房每平米均价', self.yuan_per_square)
        make_snapshot(snapshot, fifth_bar.render(), "{}\\{}.gif".format(save_dir, '五线城市二手房每平米均价'))
        print("完成二手房每平米均价作图")

    # 每套房均价
    def avg_loupan_price(self, collections):
        save_dir = self.path + "\\avg_loupan"
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
                if city in lianjia_citys['first']:
                    first_key.append(city)
                    first_value.append(int(average_price[0]['total_price_avg']))
                if city in lianjia_citys['new_first']:
                    new_first_key.append(city)
                    new_first_value.append(int(average_price[0]['total_price_avg']))
                if city in lianjia_citys['second']:
                    second_key.append(city)
                    second_value.append(int(average_price[0]['total_price_avg']))
                if city in lianjia_citys['third']:
                    third_key.append(city)
                    third_value.append(int(average_price[0]['total_price_avg']))
                if city in lianjia_citys['forth']:
                    forth_key.append(city)
                    forth_value.append(int(average_price[0]['total_price_avg']))
                if city in lianjia_citys['fifth']:
                    fifth_key.append(city)
                    fifth_value.append(int(average_price[0]['total_price_avg']))
            self.avg_price_square_meter.append(dict)
        first_bar = self.charts.bar(first_key, first_value, "", '一线城市二手房每套均价', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, first_bar.render(), "{}\\{}.gif".format(save_dir, '一线城市二手房每套均价', ))
        new_first_bar = self.charts.bar(new_first_key[:10], new_first_value[:10], "",
                                        '新一线城市二手房每套均价(1)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, new_first_bar.render(), "{}\\{}.gif".format(save_dir, '新一线城市二手房每套均价(1)', ))
        new_first_bar2 = self.charts.bar(new_first_key[10:], new_first_value[10:], "",
                                         '新一线城市二手房每套均价(2)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, new_first_bar2.render(), "{}\\{}.gif".format(save_dir, '新一线城市二手房每套均价(2)', ))
        second_bar = self.charts.bar(second_key[:10], second_value[:10], "",
                                     '二线城市二手房每套均价(1)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, second_bar.render(), "{}\\{}.gif".format(save_dir,
                                                                         '二线城市二手房每套均价(1)'))
        second_bar2 = self.charts.bar(second_key[10:20], second_value[10:20], "",
                                      '二线城市二手房每套均价(2)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, second_bar2.render(), "{}\\{}.gif".format(save_dir,
                                                                          '二线城市二手房每套均价(2)'))
        second_bar3 = self.charts.bar(second_key[20:], second_value[20:], "",
                                      '二线城市二手房每套均价(3)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, second_bar3.render(), "{}\\{}.gif".format(save_dir,
                                                                          '二线城市二手房每套均价(3)'))
        third_bar = self.charts.bar(third_key[:10], third_value[:10], "",
                                    '三线城市二手房每套均价(1)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, third_bar.render(), "{}\\{}.gif".format(save_dir, '三线城市二手房每套均价(1)'))
        third_bar2 = self.charts.bar(third_key[10:20], third_value[10:20], "",
                                     '三线城市二手房每套均价(2)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, third_bar2.render(), "{}\\{}.gif".format(save_dir, '三线城市二手房每套均价(2)'))
        third_bar3 = self.charts.bar(third_key[20:], third_value[20:], "",
                                     '三线城市二手房每套均价(3)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, third_bar3.render(), "{}\\{}.gif".format(save_dir, '三线城市二手房每套均价(3)'))
        forth_bar = self.charts.bar(forth_key[:10], forth_value[:10], "",
                                    '四线城市二手房每套均价(1)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, forth_bar.render(), "{}\\{}.gif".format(save_dir, '四线城市二手房每套均价(1)'))
        forth_bar2 = self.charts.bar(forth_key[10:20], forth_value[10:20], "",
                                     '四线城市二手房每套均价(2)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, forth_bar2.render(), "{}\\{}.gif".format(save_dir, '四线城市二手房每套均价(2)'))
        forth_bar3 = self.charts.bar(forth_key[20:], forth_value[20:], "",
                                     '四线城市二手房每套均价(3)', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, forth_bar3.render(), "{}\\{}.gif".format(save_dir, '四线城市二手房每套均价(3)'))
        fifth_bar = self.charts.bar(fifth_key, fifth_value, "",
                                    '五线城市二手房每套均价', self.ten_thousand_per_loupan)
        make_snapshot(snapshot, fifth_bar.render(), "{}\\{}.gif".format(save_dir, '五线城市二手房每套均价'))
        print("完成二手房每套均价作图")

    # 每平米最贵的top5楼盘
    def square_meter_max_top5(self, collections):
        save_dir = self.path + "\\square_meter_max_top5"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        for city in collections:
            max_top5 = list(self.db[city].aggregate(
                [
                    {'$match': {'unit_price': {'$ne': -1}}},
                    {'$sort': {'unit_price': -1}},
                    {'$limit': 5},
                    {'$project': {'unit_price': 1, 'xiaoqu_name': 1, '_id': 0, 'position': 1}}
                ]
            ))
            if max_top5:
                if max_top5[0]['xiaoqu_name'] != '':
                    key = [i['xiaoqu_name'] for i in max_top5]
                else:
                    key = [i['position'] for i in max_top5]
                value = [i['unit_price'] for i in max_top5]
            max_top5_scatter = self.charts.scatter_spliteline(key, value, city,
                                                                   self.square_price_max_top5.format(city))
            make_snapshot(snapshot, max_top5_scatter.render(),
                          "{}\\{}.gif".format(save_dir, self.square_price_max_top5.format(city)))
            print('完成 {} 每平米最贵top5小区作图'.format(city))

    # 每平米最便宜的top5楼盘
    def square_meter_min_top5(self, collections):
        save_dir = self.path + "\\square_meter_min_top5"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        for city in collections:
            min_top5 = list(self.db[city].aggregate(
                [
                    {'$match': {'unit_price': {'$ne': -1}}},
                    {'$sort': {'unit_price': 1}},
                    {'$limit': 5},
                    {'$project': {'unit_price': 1, 'xiaoqu_name': 1, '_id': 0, 'position': 1}}
                ]
            ))
            if min_top5:
                if min_top5[0]['xiaoqu_name'] != '':
                    key = [i['xiaoqu_name'] for i in min_top5]
                else:
                    key = [i['position'] for i in min_top5]
                value = [i['unit_price'] for i in min_top5]
            min_top5_scatter = self.charts.scatter_visualmap_color(key, value, city,
                                                                   self.square_price_min_top5.format(city))
            make_snapshot(snapshot, min_top5_scatter.render(),
                          "{}\\{}.gif".format(save_dir, self.square_price_min_top5.format(city)))
            print('完成 {} 每平米最便宜top5小区作图'.format(city))

    # 热门小区词云
    def xiaoqu_wordcloud(self, collections):
        save_dir = self.path + "\\xiaoqu_wordcloud"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        for city in collections:
            xiaoqu = {}
            wordcloud = []
            result = list(self.db[city].aggregate(
                [
                    {'$match': {'xiaoqu_name': {'$ne': ''}}},
                    {'$project': {'xiaoqu_name': 1, '_id': 0}},
                ]
            ))
            for x in result:
                xiaoqu[x['xiaoqu_name']] = 0
            for x in result:
                xiaoqu[x['xiaoqu_name']] += 1
            for key, value in xiaoqu.items():
                wordcloud.append((key, value))
            xiaoqu_wordcloud = self.charts.wordcloud_diamond(wordcloud, title='{}市二手房热门小区'.format(city))
            make_snapshot(snapshot, xiaoqu_wordcloud.render(),
                          "{}\\{}.gif".format(save_dir, '{}市二手房热门小区'.format(city)))
            print("完成{}市热门小区词云".format(city))

    # 热门地段词云
    def position_wordcloud(self, collections):
        save_dir = self.path + "\\position_wordcloud"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        for city in collections:
            position = {}
            wordcloud = []
            result = list(self.db[city].aggregate(
                [
                    {'$match': {'position': {'$ne': ''}}},
                    {'$project': {'position': 1, '_id': 0}},
                ]
            ))
            for x in result:
                position[x['position']] = 0
            for x in result:
                position[x['position']] += 1
            for key, value in position.items():
                wordcloud.append((key, value))
            position_wordcloud = self.charts.wordcloud_diamond(wordcloud, title='{}市二手房热门地段'.format(city))
            make_snapshot(snapshot, position_wordcloud.render(),
                          "{}\\{}.gif".format(save_dir, '{}市二手房热门地段'.format(city)))
            print("完成{}市二手房热门地段词云".format(city))

