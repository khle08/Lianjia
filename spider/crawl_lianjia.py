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
    logging.info('成功进入{}'.format(os.getcwd()))
    rent_crawl = os.system('scrapy crawl rent')


def crawl_lianjia():
    one = threading.Thread(target=crawl_ershoufang)
    one.start()
    two = threading.Thread(target=crawl_newhouse)
    two.start()
    three = threading.Thread(target=crawl_rent)
    three.start()


if __name__ == '__main__':
    one = threading.Thread(target=crawl_ershoufang)
    one.start()
    two = threading.Thread(target=crawl_newhouse)
    two.start()
    three = threading.Thread(target=crawl_rent)
    three.start()
