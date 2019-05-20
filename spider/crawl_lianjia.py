import os
import logging
from config import *
import time

def crawl_ershoufang():
    print(os.getcwd())
    ershoufang_dir = os.chdir('lianjia_ershoufang')
    logging.info('成功进入{}'.format(os.getcwd()))
    ershoufang_crawl = os.system('scrapy crawl ershoufang')


def crawl_newhouse():
    print(os.getcwd())
    newhouse_dir = os.chdir('lianjia_newhouse')
    logging.info('成功进入{}'.format(os.getcwd()))
    newhouse_crawl = os.system('scrapy crawl newhouse')


def crawl_rent():
    print(os.getcwd())
    rent_dir = os.chdir('lianjia_rent')
    logging.info('成功进入{}'.format(os.getcwd()))
    rent_crawl = os.system('scrapy crawl rent')


def crawl_lianjia():
    os.chdir('spider')
    spider_status = '正在爬取二手房数据'
    crawl_ershoufang()
    spider_status = '正在爬取新房数据'
    crawl_newhouse()
    spider_status = '正在爬取租房数据'
    crawl_rent()
    data_update_time = int(time.time())
    os.chdir('..')