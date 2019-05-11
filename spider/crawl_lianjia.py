import threading
import os
import logging


def crawl_ershoufang():
    ershoufang_dir = os.chdir('lianjia_ershoufang')
    logging.info('成功进入{}'.format(os.getcwd()))
    ershoufang_crawl = os.system('scrapy crawl ershoufang')



def crawl_newhouse():
    newhouse_dir = os.chdir('lianjia_newhouse')
    logging.info('成功进入{}'.format(os.getcwd()))
    newhouse_crawl = os.system('scrapy crawl newhouse')


def crawl_rent():
    rent_dir = os.chdir('lianjia_rent')
    rent_crawl = os.system('scrapy crawl rent')
    logging.info('成功进入{}'.format(os.getcwd()))
    # ershoufang = threading.Thread(target=run_ershoufang, name='二手房')
    # new_house = threading.Thread(target=run_newhouse, name='新房')
    # rent_house = threading.Thread(target=run_rent, name='租房')
