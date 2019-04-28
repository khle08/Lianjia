import threading
from spider.lianjia_ershoufang.lianjia_ershoufang.run import run_ershoufang
from spider.lianjia_newhouse.lianjia_newhouse.run import run_newhouse
from spider.lianjia_rent.lianjia_rent.run import run_rent
import os


def crawl_lianjia():
    # ershoufang = threading.Thread(target=run_ershoufang, name='二手房')
    # new_house = threading.Thread(target=run_newhouse, name='新房')
    # rent_house = threading.Thread(target=run_rent, name='租房')
    # ershoufang.start()
    # new_house.start()
    # rent_house.start()
    print("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))
