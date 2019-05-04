from lianjia.constants import *
import os
from data_visualize.common import base_path


class newhouse_list():
    def __init__(self, city, analysis):
        data = []
        self.city = city
        self.analysis = analysis
        self.img_base_path = "/static/newhouse"
        self.result = {
            1: self.main_price_range(city),
            2: self.second_price_range(city),
            3: self.avg_square_meter(city),
            4: self.avg_loupan_price(city),
            5: self.wuye_type_count(city),
            6: self.huxing_count(city),
            7: self.square_meter_max_top5(city),
            8: self.square_meter_min_top5(city),
            9: self.tag_wordcloud(city)
        }

    # 返回数据给前端
    def parse(self):
        return self.result[self.analysis]

    # 每平米价位占比
    def main_price_range(self, city):
        city_map = get_city_map('newhouse')
        data = []
        data.append(self.img_base_path + "/main_price_range/{}市新房每平米楼盘价位占比分布图.gif".format(city_map[city]))
        return data

    # 每套房各价位占比
    def second_price_range(self, city):
        city_map = get_city_map('newhouse')
        data = []
        data.append(self.img_base_path + "/second_price_range/{}市每套新房价位占比分布图.gif".format(city_map[city]))
        return data

    # 每平米均价
    def avg_square_meter(self, city):
        img_list = [
            self.img_base_path + '/avg_square_meter/链家部分一线城市及新一线城市新房每平米均价.gif',
            self.img_base_path + '/avg_square_meter/链家部分二线内陆城市新房每平米均价.gif',
            self.img_base_path + '/avg_square_meter/链家部分二线沿海城市新房每平米均价.gif',
            self.img_base_path + '/avg_square_meter/链家部分三线城市新房每平米均价.gif',
            self.img_base_path + '/avg_square_meter/链家部分四线城市新房每平米均价.gif',
            self.img_base_path + '/avg_square_meter/链家部分五线城市新房每平米均价.gif',
        ]
        return img_list

    # 每套房均价
    def avg_loupan_price(self, city):
        img_list = [
            self.img_base_path + '/avg_loupan/链家部分一线城市及新一线城市每套新房均价.gif',
            self.img_base_path + '/avg_loupan/链家部分二线内陆城市每套新房均价.gif',
            self.img_base_path + '/avg_loupan/链家部分二线沿海城市每套新房均价.gif',
            self.img_base_path + '/avg_loupan/链家部分三线城市每套新房均价.gif',
            self.img_base_path + '/avg_loupan/链家部分四线城市每套新房均价.gif',
            self.img_base_path + '/avg_loupan/链家部分五线城市每套新房均价.gif',
        ]
        return img_list

    # 物业占比分布图
    def wuye_type_count(self, city):
        city_map = get_city_map('newhouse')
        data = []
        data.append(self.img_base_path + "/wuye_type_count/{}市新房物业类型占比分布图.gif".format(city_map[city]))
        return data

    # 各户型占比
    def huxing_count(self, city):
        city_map = get_city_map('newhouse')
        data = []
        data.append(self.img_base_path + "/huxing_count/{}市新房户型占比分布图.gif".format(city_map[city]))
        return data

    # 每平米最贵的top5楼盘
    def square_meter_max_top5(self, city):
        city_map = get_city_map('newhouse')
        data = []
        data.append(self.img_base_path + "/square_meter_max_top5/{}市新房每平米最贵top5楼盘.gif".format(city_map[city]))
        return data

    # 每平米最便宜的top5楼盘
    def square_meter_min_top5(self, city):
        city_map = get_city_map('newhouse')
        data = []
        data.append(self.img_base_path + "/square_meter_min_top5/{}市新房每平米最便宜top5楼盘.gif".format(city_map[city]))
        return data

    # 标签词云
    def tag_wordcloud(self, city):
        city_map = get_city_map('newhouse')
        data = []
        data.append(self.img_base_path + "/tag_wordcloud/{}市新房热门标签.gif".format(city_map[city]))
        return data


class ershoufang_list():
    def __init__(self, city, analysis):
        data = []
        self.city = city
        self.analysis = analysis
        self.img_base_path = "/static/ershoufang"
        self.result = {
            1: self.unit_price_range(city),
            2: self.total_price_range(city),
            3: self.avg_square_meter(city),
            4: self.avg_loupan_price(city),
            5: self.square_meter_max_top5(city),
            6: self.square_meter_min_top5(city),
            7: self.xiaoqu_wordcloud(city),
            8: self.position_wordcloud(city)
        }

    # 返回数据给前端
    def parse(self):
        return self.result[self.analysis]

    # 每平米价位占比
    def unit_price_range(self, city):
        city_map = get_city_map('ershoufang')
        data = []
        data.append(self.img_base_path + "/unit_price_range/{}市二手房每平米楼盘价位占比分布图.gif".format(city_map[city]))
        return data

    # 每套房各价位占比
    def total_price_range(self, city):
        city_map = get_city_map('ershoufang')
        data = []
        data.append(self.img_base_path + "/total_price_range/{}市二手房每套房价位占比分布图.gif".format(city_map[city]))
        return data

    # 每平米均价
    def avg_square_meter(self, city):
        img_list = [
            self.img_base_path + '/avg_square_meter/一线城市二手房每平米均价.gif',
            self.img_base_path + '/avg_square_meter/新一线城市二手房每平米均价(1).gif',
            self.img_base_path + '/avg_square_meter/新一线城市二手房每平米均价(2).gif',
            self.img_base_path + '/avg_square_meter/二线城市二手房每平米均价(1).gif',
            self.img_base_path + '/avg_square_meter/二线城市二手房每平米均价(2).gif',
            self.img_base_path + '/avg_square_meter/二线城市二手房每平米均价(3).gif',
            self.img_base_path + '/avg_square_meter/三线城市二手房每平米均价(1).gif',
            self.img_base_path + '/avg_square_meter/三线城市二手房每平米均价(2).gif',
            self.img_base_path + '/avg_square_meter/三线城市二手房每平米均价(3).gif',
            self.img_base_path + '/avg_square_meter/四线城市二手房每平米均价(1).gif',
            self.img_base_path + '/avg_square_meter/四线城市二手房每平米均价(2).gif',
            self.img_base_path + '/avg_square_meter/四线城市二手房每平米均价(3).gif',
            self.img_base_path + '/avg_square_meter/五线城市二手房每平米均价.gif',
        ]
        return img_list

    # 每套房均价
    def avg_loupan_price(self, city):
        img_list = [
            self.img_base_path + '/avg_loupan/一线城市二手房每套均价.gif',
            self.img_base_path + '/avg_loupan/新一线城市二手房每套均价(1).gif',
            self.img_base_path + '/avg_loupan/新一线城市二手房每套均价(2).gif',
            self.img_base_path + '/avg_loupan/二线城市二手房每套均价(1).gif',
            self.img_base_path + '/avg_loupan/二线城市二手房每套均价(2).gif',
            self.img_base_path + '/avg_loupan/二线城市二手房每套均价(3).gif',
            self.img_base_path + '/avg_loupan/三线城市二手房每套均价(1).gif',
            self.img_base_path + '/avg_loupan/三线城市二手房每套均价(2).gif',
            self.img_base_path + '/avg_loupan/三线城市二手房每套均价(3).gif',
            self.img_base_path + '/avg_loupan/四线城市二手房每套均价(1).gif',
            self.img_base_path + '/avg_loupan/四线城市二手房每套均价(2).gif',
            self.img_base_path + '/avg_loupan/四线城市二手房每套均价(3).gif',
            self.img_base_path + '/avg_loupan/五线城市二手房每套均价.gif',
        ]
        return img_list

    # 每平米最贵的top5楼盘
    def square_meter_max_top5(self, city):
        city_map = get_city_map('ershoufang')
        data = []
        data.append(self.img_base_path + "/square_meter_max_top5/{}市二手房每平米最贵top5小区.gif".format(city_map[city]))
        return data

    # 每平米最便宜的top5楼盘
    def square_meter_min_top5(self, city):
        city_map = get_city_map('ershoufang')
        data = []
        data.append(self.img_base_path + "/square_meter_min_top5/{}市二手房每平米最便宜top5小区.gif".format(city_map[city]))
        return data

    # 热门小区词云
    def xiaoqu_wordcloud(self, city):
        city_map = get_city_map('ershoufang')
        data = []
        data.append(self.img_base_path + "/xiaoqu_wordcloud/{}市二手房热门小区.gif".format(city_map[city]))
        return data

    # 热门地段词云
    def position_wordcloud(self, city):
        city_map = get_city_map('ershoufang')
        data = []
        data.append(self.img_base_path + "/position_wordcloud/{}市二手房热门地段.gif".format(city_map[city]))
        return data


class rent_list():
    def __init__(self, city, analysis):
        data = []
        self.city = city
        self.analysis = analysis
        self.img_base_path = "/static/rent"
        self.result = {1: self.source_percentage(city),
                       2: self.brandtop5_avg_price(city),
                       3: self.avg_price_rent(city),
                       4: self.rent_max_top5(city),
                       5: self.rent_min_top5(city),
                       6: self.tag_wordcloud(city)
                       }

    # 返回数据给前端
    def parse(self):
        return self.result[self.analysis]

    #  每个品牌房源占比
    def source_percentage(self, city):
        city_map = get_city_map('rent')
        data = []
        data.append(self.img_base_path + "/source_percentage/{}市链家租房来源.gif".format(city_map[city]))
        return data

    # 房源占比最高的top5均价
    def brandtop5_avg_price(self, city):
        city_map = get_city_map('rent')
        data = []
        data.append(self.img_base_path + "/brand_avg_price/{}市房源占比最高平台top5均价.gif".format(city_map[city]))
        return data

    # 每平米均价
    def avg_price_rent(self, city):
        img_list = [
            self.img_base_path + '/avg_price/一线城市租房均价.gif',
            self.img_base_path + '/avg_price/新一线城市租房均价(1).gif',
            self.img_base_path + '/avg_price/新一线城市租房均价(2).gif',
            self.img_base_path + '/avg_price/二线城市租房均价(1).gif',
            self.img_base_path + '/avg_price/二线城市租房均价(2).gif',
            self.img_base_path + '/avg_price/二线城市租房均价(3).gif',
            self.img_base_path + '/avg_price/三线城市租房均价(1).gif',
            self.img_base_path + '/avg_price/三线城市租房均价(2).gif',
            self.img_base_path + '/avg_price/三线城市租房均价(3).gif',
            self.img_base_path + '/avg_price/四线城市租房均价(1).gif',
            self.img_base_path + '/avg_price/四线城市租房均价(2).gif',
            self.img_base_path + '/avg_price/四线城市租房均价(3).gif',
            self.img_base_path + '/avg_price/五线城市租房均价.gif',
        ]
        return img_list

    # 租房最贵top5
    def rent_max_top5(self, city):
        city_map = get_city_map('rent')
        data = []
        data.append(self.img_base_path + "/rent_max_top5/{}市租房价格最高top5.gif".format(city_map[city]))
        return data

    # 租房最低top5
    def rent_min_top5(self, city):
        city_map = get_city_map('rent')
        data = []
        data.append(self.img_base_path + "/rent_min_top5/{}市租房价格最低top5.gif".format(city_map[city]))
        return data

    # 租房标签词云
    def tag_wordcloud(self, city):
        city_map = get_city_map('rent')
        data = []
        data.append(self.img_base_path + "/tag_wordcloud/{}市租房热门标签.gif".format(city_map[city]))
        return data
