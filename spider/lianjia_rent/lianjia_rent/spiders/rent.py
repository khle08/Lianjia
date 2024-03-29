# -*- coding: utf-8 -*-
import scrapy
from ..common import *
from scrapy import Request
import time
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
        soup = BeautifulSoup(response.text, 'lxml')
        list = soup.find_all(attrs={'class': 'content__list--item'})
        for div in list:
            item = LianjiaRentItem()
            item['city'] = self.city
            temp = div.find_all(attrs={'class': 'content__list--item--title twoline'})
            if temp:
                temp = temp[0].find_all(attrs={'target': '_blank'})
                if temp:
                    item['house'] = temp[0].text.replace('\n', '').strip()
                    item['zufang_url'] = self.city_url + temp[0].attrs['href'][1:]
                else:
                    item['house'] = NOT_EXIST_STR
                    item['zufang_url'] = NOT_EXIST_STR
            else:
                item['house'] = NOT_EXIST_STR
                item['zufang_url'] = NOT_EXIST_STR
            temp = div.find_all(attrs={'class': 'content__list--item--des'})
            if temp:
                item['district_multi'] = temp[0].text.replace('\n', '').replace(' ', '').split('/')
            else:
                item['district_multi'] = NOT_EXIST_LIST
            temp = div.find_all(attrs={'class': 'content__list--item--brand oneline'})
            if temp:
                item['brand'] = temp[0].text.strip()
            else:
                item['brand'] = NOT_EXIST_STR
            temp = div.find_all(attrs={'class': 'content__list--item--aside'})
            if temp:
                item['img_url'] = temp[0].img['data-src']
            else:
                item[
                    'img_url'] = 'https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182_1.png?_v=201905091318410f3'
            temp = div.find_all(attrs={'class': 'content__list--item-price'})
            if temp:
                temp = temp[0].text.replace(' ', '').replace('元/月', '')
                if temp.isdigit():
                    item['price'] = int(temp)
                else:
                    item['price'] = temp
            else:
                item['price'] = NOT_EXIST_NUM
            if item['price'] == NOT_EXIST_NUM:
                continue
            temp = div.find_all(attrs={'class': 'content__list--item--time oneline'})
            if temp:
                item['post_time'] = temp[0].text.replace(' ', '').strip()
            else:
                item['post_time'] = NOT_EXIST_STR
            temp = div.find_all(attrs={'class': 'content__list--item--bottom oneline'})
            if temp:
                item['tag'] = temp[0].text.split('\n')[1:-1]
            else:
                item['tag'] = NOT_EXIST_LIST
            item['crawl_time'] = int(time.time())
            yield item
