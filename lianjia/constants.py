import pymongo
import time
import os

ershoufang_db = ''
web_static_base_path = os.path.split(os.path.realpath(__file__))[0] + "\\static"


def get_city_form(type):
    client = pymongo.MongoClient()
    db = 'lianjia_{}'.format(type) + str(time.strftime('%Y%m%d', time.localtime(time.time())))
    db = client[db]
    collections = db.list_collection_names()
    list = [(-1, '请选择城市:'), ]
    count = 1
    for i in collections:
        list.append((count, i))
        count += 1
    return list


def get_city_map(type):
    client = pymongo.MongoClient()
    db = 'lianjia_{}'.format(type) + str(time.strftime('%Y%m%d', time.localtime(time.time())))
    db = client[db]
    collections = db.list_collection_names()
    dict = {}
    count = 1
    for i in collections:
        dict[count] = i
        count += 1
    return dict


newhouse_city_form = get_city_form('newhouse')
newhouse_city_map = get_city_map('newhouse')
ershoufang_city_form = get_city_form('ershoufang')
ershoufang_city_map = get_city_map('ershoufang')
rent_city_form = get_city_form('rent')
rent_city_map = get_city_map('rent')

newhouse_analysis_form = [(0, '请选择视角:'), (1, '每平米价位占比'), (2, '每套房价位占比'),
                          (3, '每平米均价'), (4, '每套房均价'),
                          (5, '物业占比分布'), (6, '户型占比分布'),
                          (7, '每平米最高top5楼盘'), (8, '每平米最低top5楼盘'), (9, '热门标签词云')]
newhouse_analysis_map = {1: '每平米价位占比', 2: '每套房价位占比',
                         3: '每平米均价', 4: '每套房均价', 5: '物业占比分布',
                         6: '户型占比分布', 7: '每平米最高top5楼盘',
                         8: '每平米最低top5楼盘', 9: '热门标签词云'}
ershoufang_analysis_form = [(0, '请选择视角:'), (1, '每平米价位占比'), (2, '每套房价位占比'), (3, '每平米均价'),
                            (4, '每套房均价'), (5, '每平米最高top5楼盘'), (6, '每平米最低top5楼盘'),
                            (7, ' 热门小区词云'), (8, '热门地段词云')]
ershoufang_analysis_map = {1: '每平米价位占比', 2: '每套房价位占比',
                           3: '每平米均价', 4: '每套房均价',
                           5: '每平米最高top5楼盘', 6: '每平米最低top5楼盘',
                           7: ' 热门小区词云', 8: '热门地段词云'}
rent_analysis_form = [(0, '请选择视角:'), (1, '每个品牌房源占比'), (2, '房源占比最高的top5均价'),
                      (3, '每平米均价'),
                      (4, '租房最高价top5'), (5, '租房最低top5'), (6, '租房标签热门词云')]
rent_analysis_map = {1: '每个品牌房源占比', 2: '房源占比最高的top5均价',
                     3: '每平米均价', 4: '租房最高价top5', 5: '租房最低top5', 6: '租房标签热门词云'}
search_type = [(0, '请选择搜索类型:'), (1, '全部'), (2, '二手房'), (3, '新房'), (4, '租房')]
search_type_map = {0: '请选择搜索类型:', 1: '全部', 2: '二手房', 3: '新房', 4: '租房'}
