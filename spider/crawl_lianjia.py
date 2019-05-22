import os
import logging
from config import *
import time
import pymongo


# 更新数据前先删除当天已经存在的数据库
def drop_database():
    client = pymongo.MongoClient()
    if client['lianjia_newhouse' + str(time.strftime('%Y%m%d', time.localtime(time.time())))]:
        client.drop_database('lianjia_newhouse' + str(time.strftime('%Y%m%d', time.localtime(time.time()))))
    if client['lianjia_ershoufang' + str(time.strftime('%Y%m%d', time.localtime(time.time())))]:
        client.drop_database('lianjia_ershoufang' + str(time.strftime('%Y%m%d', time.localtime(time.time()))))
    if client['lianjia_rent' + str(time.strftime('%Y%m%d', time.localtime(time.time())))]:
        client.drop_database('lianjia_rent' + str(time.strftime('%Y%m%d', time.localtime(time.time()))))


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
    print(os.getcwd())
    drop_database()
    spider_status = '正在爬取二手房数据'
    crawl_ershoufang()
    spider_status = '正在爬取新房数据'
    print(os.getcwd())
    crawl_newhouse()
    spider_status = '正在爬取租房数据'
    print(os.getcwd())
    crawl_rent()
    data_update_time = int(time.time())
    os.chdir(os.pardir)
    print(os.getcwd())
