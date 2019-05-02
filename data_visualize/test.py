from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Scatter
import pymongo
import time
from data_visualize.echarts import charts
import os
from data_visualize.common import *
from pyecharts.render import make_snapshot
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot

lianjia_ershoufang_citys = {}
lianjia_ershoufang_citys['first'] = [ '北京','深圳', '广州','上海',  ]
lianjia_ershoufang_citys['new_first'] = ['长沙','苏州', '青岛', '武汉', '大连', '天津','沈阳',
                                         '郑州','成都',  '杭州','宁波','东莞','南京', '西安','重庆',]
lianjia_ershoufang_citys['second'] = ['长春', '常州','台州', '南宁','合肥','珠海', '无锡', '石家庄',
                                      '昆明', '贵阳', '金华', '哈尔滨', '中山','嘉兴','太原','温州',
                                      '海口', '泉州','惠州','厦门', '兰州','福州','南通','佛山','济南',
                                      '烟台','绍兴','南昌',]
lianjia_ershoufang_citys['third'] = ['九江','南充', '盐城','岳阳', '保定',  '清远','上饶','襄阳','丹东',
                                     '江门','龙岩','秦皇岛','镇江', '柳州','威海','洛阳','湛江','马鞍山',
                                     '芜湖', '廊坊',  '湖州', '淮安', '绵阳','宜昌','漳州', '桂林','株洲',
                                     '银川', '临沂', '淄博','呼和浩特','赣州','昆山',  '三亚','唐山','潍坊',]
lianjia_ershoufang_citys['forth'] = ['承德','大理','滁州','许昌','眉山', '咸宁','常德','张家口',
                                     '开封','黄石', '德阳',  '黄冈','新乡','晋中', '西双版纳','吉安',
                                     '安庆', '乐山','邢台','咸阳', '吉林','宝鸡', '北海',]
lianjia_ershoufang_citys['fifth'] = ['凉山', '达州','汉中',  '临高','保亭',]
