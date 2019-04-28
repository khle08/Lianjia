# -*- coding: utf-8 -*-
import scrapy
from ..common import *
from scrapy import Request
import time
from scrapy.log import logger
from bs4 import BeautifulSoup
from ..items import LianjiaRentItem


class RentSpider(scrapy.Spider):
    name = 'rent'
    allowed_domains = ['lianjia.com']
    start_urls = []
    house = []
    city_url = ''
    city = ''

    def __int__(self):
        self.start_urls = get_all_city()
        self.city_map = all_city_map()

    def start_requests(self):
        for city, url in all_city_map().items():
            self.city_url = url
            self.city = city
            for i in range(1, 101):
                crawl_url = '{}/zufang/pg{}'.format(url, str(i))
                yield Request(crawl_url, self.parse, dont_filter=True)

    def parse(self, response):
        soup = BeautifulSoup(response.text,'lxml')
        content = soup.find_all(attrs={'class':'content__list--item'})
        print(len(content))
