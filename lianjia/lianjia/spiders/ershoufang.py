# -*- coding: utf-8 -*-
import scrapy
from ..all_city import *
import re
from scrapy import Request
from ..items import LianjiaItem
import time


class LianjiahouseSpider(scrapy.Spider):
    name = 'ershoufang'
    allowed_domains = ['www.lianjia.com']
    start_urls = []
    house = []

    def __int__(self):
        self.start_urls = get_all_city()
        self.city_map = all_city_map()

    def start_requests(self):
        for city, url in all_city_map().items():
            for i in range(1, 101):
                crawl_url = '{}/pg{}/'.format(url, str(i))
                yield Request(crawl_url, self.parse, dont_filter=True)

    def parse(self, response):
        city = re.findall(re.compile("city_name: '(.+?)'"), response.text)[0]
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
            item = LianjiaItem()
            item['city'] = city
            item['house_url'] = url[i]
            if len(img_title[i][0]) > 120:
                item['img_url'] = img_title[i][0].split('">')[0]
            else:
                item['img_url'] = img_title[i][0]
            item['title'] = img_title[i][1]
            item['xiaoqu_url'] = xiaoqu[i]['xiaoqu_url']
            item['xiaoqu_name'] = xiaoqu[i]['xiaoqu_name']
            item['huxing'] = xiaoqu[i]['huxing']
            item['position_info'] = position_info[i]['position_info']
            item['position'] = position_info[i]['position']
            item['position_url'] = position_info[i]['position_url']
            item['total_price'] = int(total_price[i]) * 10000
            item['unit_price'] = int(unit_price[i])
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
