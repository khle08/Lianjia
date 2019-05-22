from data_visualize.newhouse import newhouse
from data_visualize.ershoufang import ershoufang
from data_visualize.rent import rent
import os
from config import *


def data_analysis():
    print(os.getcwd())
    os.chdir('data_visualize')
    data_analysis_status = '正在进行二手房数据分析'
    one = ershoufang()
    data_analysis_status = '正在进行新房数据分析'
    two = newhouse()
    data_analysis_status = '正在进行租房数据分析'
    three = rent()
    os.chdir(os.pardir)
    print(os.getcwd())
