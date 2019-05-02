# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
from ..common import *
from ..items import LianjiaErshoufangItem
import time


class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'
    allowed_domains = ['lianjia.com']
    start_urls = []
    house = []
    city = ''
    def __int__(self):
        self.start_urls = get_all_city()
        self.city_map = all_city_map()

    def start_requests(self):
        for city, url in all_city_map().items():
            self.city = city
            for i in range(1, 101):
                crawl_url = '{}/ershoufang/pg{}/'.format(url, str(i))
                yield Request(crawl_url, self.parse, dont_filter=True)

    def parse(self, response):
        url = re.findall(re.compile('<a class="noresultRecommend img " href="(.+?)"'),
                         response.text)
        img_title = re.findall(re.compile('data-original="(.+?)" alt="(.+?)"></a><div class="info clear">?'),
                               response.text)
        xiaoqu = self.get_xiaoqu(re.findall(re.compile('<div class="address">(.+?)</div>'),
                                            response.text))
        position_info = self.get_position_info(
            re.findall(re.compile('<div class="positionInfo">(.+?)</div>'), response.text))
        total_price = re.findall(re.compile('class="totalPrice"><span>(.+?)</span>'),
                                 response.text)
        unit_price = re.findall(re.compile('<div class="unitPrice" .*? data-price="(\d+)">'),
                                response.text)
        for i in range(len(url)):
            item = LianjiaErshoufangItem()
            item['city'] = self.city
            if url[i]:
                item['house_url'] = url[i]
            else:
                item['house_url'] = NOT_EXIST_STR
            if img_title[i][0]:
                if len(img_title[i][0]) > 120:
                    item['img_url'] = img_title[i][0].split('">')[0]
                else:
                    item['img_url'] = img_title[i][0]
            else:
                item['img_url'] = NOT_EXIST_STR
            if img_title[i][1]:
                item['title'] = img_title[i][1]
            else:
                item['title'] = NOT_EXIST_STR
            if xiaoqu[i]['xiaoqu_url']:
                item['xiaoqu_url'] = xiaoqu[i]['xiaoqu_url']
            else:
                item['xiaoqu_url'] = NOT_EXIST_STR
            if xiaoqu[i]['xiaoqu_name']:
                item['xiaoqu_name'] = xiaoqu[i]['xiaoqu_name']
            else:
                item['xiaoqu_name'] = NOT_EXIST_STR
            if xiaoqu[i]['huxing']:
                item['huxing'] = xiaoqu[i]['huxing']
            else:
                item['huxing'] = NOT_EXIST_STR
            if position_info[i]['position_info']:
                item['position_info'] = position_info[i]['position_info']
            else:
                item['position_info'] = NOT_EXIST_STR
            if position_info[i]['position']:
                item['position'] = position_info[i]['position']
            else:
                item['position'] = NOT_EXIST_STR
            if position_info[i]['position_url']:
                item['position_url'] = position_info[i]['position_url']
            else:
                item['position_url'] = NOT_EXIST_STR
            if total_price[i].isdigit():
                item['total_price'] = int(total_price[i])
            else:
                item['total_price'] = NOT_EXIST_NUM
            if unit_price[i].isdigit():
                item['unit_price'] = int(unit_price[i])
            else:
                item['unit_price'] = NOT_EXIST_NUM
            item['crawl_time'] = int(time.time())
            yield item

    def get_xiaoqu(self, xiaoqu):
        list = []
        for x in xiaoqu:
            dict = {}
            dict['xiaoqu_url'] = ''.join(re.findall(re.compile('<a href="(.+?)"'), x))
            dict['xiaoqu_name'] = ''.join(re.findall(re.compile('data-el="region">(.+?)</a>'), x))
            try:
                x = x.replace('<div class="houseInfo">', '').replace('<span class="divide">/</span>', ''). \
                    replace('</div>', '').replace('</a>', '')
                x = re.compile('</?\w+[^>]*>').sub('', x)
                dict['huxing'] = x.split('|')
            except:
                dict['huxing'] = ''
            list.append(dict)
        return list

    def get_position_info(self, position):
        list = []
        for p in position:
            dict = {}
            dict['position_info'] = ''.join(re.findall(re.compile('</span>(.+?)<a'), p)).replace(
                '<span class="divide">/</span>', ''
            ).replace(' ', '')
            dict['position'] = ''.join(re.findall(re.compile('target="_blank">(.+?)</a>'), p))
            dict['position_url'] = ''.join(re.findall(re.compile('href="(.+?)"'), p))
            list.append(dict)
        return list
