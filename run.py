from data_visualize.data_analysis import data_analysis
from spider.crawl_lianjia import crawl_lianjia
from lianjia.app import app
import time
from config import *

if __name__ == '__main__':
    init_time = int(time.time())
    while True:
        if (int(time.time()) - init_time) % data_update_frequency == 0:
            spider = crawl_lianjia()
            data = data_analysis()
            web = app.run()
