import time
import pymongo

base_path = "D:\codes\GraduationProject\data_visualize"
# 字符串模板
main_price_range_template = '{}市每平米楼盘价位占比分布图'
second_price_range_template = '{}市'

# 每平米最高统计500000每平米的房价
max_main_price = 500000
# 每套房统计最高1亿的价格
max_second_price = 10000


# 生成每平米价格的范围过滤条件
def gen_match(price, delta):
    price_range_map = {}
    for i in range(0, price + delta, delta):
        price_range_map['{}-{}'.format(i, i + delta)] = {
            '$gte': i,
            '$lt': i + delta
        }
    return price_range_map


# 获取main_price各区间分布
def get_main_price_range(city):
    client = pymongo.MongoClient()
    db = 'lianjia_newhouse' + str(time.strftime('%Y%m%d', time.localtime(time.time())))
    db = client[db]
    collection = db[city]
    price = max_main_price
    while price > 1000:
        result = list(collection.find({'main_price': {'$gte': price}}))
        if result:
            if price > 100000:
                return gen_match(price, 20000)
            if price > 50000:
                return gen_match(price, 10000)
            if price > 30000:
                return gen_match(price, 5000)
            return gen_match(price, 3000)
        else:
            price = int(price / 2)


# 获取second_price各区间分布
def get_second_price_range(city):
    client = pymongo.MongoClient()
    db = 'lianjia_newhouse' + str(time.strftime('%Y%m%d', time.localtime(time.time())))
    db = client[db]
    collection = db[city]
    price = max_second_price
    while price > 10:
        result = list(collection.find({'second_price': {'$gte': price}}))
        if result:
            if price > 5000:
                return gen_match(price, 1000)
            if price > 3000:
                return gen_match(price, 400)
            if price > 1000:
                return gen_match(price, 200)
            if price > 500:
                return gen_match(price, 70)
            if price > 200:
                return gen_match(price, 30)
            return gen_match(price, 15)
        price = int(price / 2)
