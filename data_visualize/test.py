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


dict =  {'age':12}
dict['sum']+=1
if dict['sum']:
    dict['sum']+=1
else:
    dict['sum'] = 0
print(dict)