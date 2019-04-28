# -*- coding: utf-8 -*-
import scrapy
from ..common import *
from scrapy import Request
import time
from scrapy.log import logger
from bs4 import BeautifulSoup
from ..items import NewhouseItem


class NewhouseSpider(scrapy.Spider):
    name = 'newhouse'
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
            page = get_new_house_page(url)
            self.city_url = url
            self.city = city
            logger.info('{} 一共有{} 页'.format(city, page))
            for i in range(1, page + 1):
                crawl_url = '{}/loupan/pg{}'.format(url, str(i))
                yield Request(crawl_url, self.parse, dont_filter=True)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        ul = soup.find_all(attrs={'class': 'resblock-list post_ulog_exposure_scroll has-results'})
        for li in ul:
            item = NewhouseItem()
            temp = li.find_all(attrs={'class': 'name'})
            if temp:
                item['loupan'] = temp[0].text
            else:
                item['loupan'] = NOT_EXIST
            item['city'] = self.city
            temp = li.find_all(attrs={'class': 'name'})
            if temp:
                item['loupan_url'] = self.city_url[:-1] + temp[0].attrs['href']
            else:
                item['loupan_url'] = NOT_EXIST
            temp = li.find_all(attrs={'class': 'resblock-type'})
            if temp:
                item['wuye_type'] = temp[0].text
            else:
                item['wuye_type'] = NOT_EXIST
            temp = li.find_all(attrs={'class': 'sale-status'})
            if temp:
                item['sale_status'] = temp[0].text
            else:
                item['sale_status'] = NOT_EXIST
            temp = li.find_all(attrs={'class': 'lj-lazy'})
            if temp:
                item['img_url'] = temp[0].attrs['data-original']
            else:
                item['img_url'] = NOT_EXIST
            temp = li.find_all(attrs={'class': 'resblock-location'})
            if temp:
                item['location'] = temp[0].text.replace('\n', '').split('/')
            else:
                item['location'] = NOT_EXIST
            temp = li.find_all(attrs={'class': 'resblock-room'})
            if temp:
                item['huxing'] = temp[0].text.replace('\n', '')
            else:
                item['huxing'] = NOT_EXIST
            temp = li.find_all(attrs={'class': 'resblock-area'})
            if temp:
                tmp_area = temp[0].text.replace(' ', '').replace('\n', '').replace('建面', '').replace('㎡', '')
                if tmp_area == '':
                    item['area'] = []
                else:
                    list = tmp_area.split('-')
                    item['area'] = []
                    for i in list:
                        if i.isdigit():
                            item['area'].append(int(i))
                        else:
                            item['area'].append(i)
            else:
                item['area'] = []
            main_price = li.find_all(attrs={'class': 'number'})
            if main_price != []:
                temp = main_price[0].text.replace(' ', '')
                if temp.isdigit():
                    item['main_price'] = int(temp)
                else:
                    item['main_price'] = temp
            else:
                item['main_price'] = NOT_EXIST
            main_price_desc = li.find_all(attrs={'class': 'desc'})
            if main_price_desc != []:
                item['main_price_desc'] = main_price_desc[0].text.replace('\xa0', '')
            else:
                item['main_price_desc'] = NOT_EXIST
            second_price = li.find_all(attrs={'class': 'second'})
            if (second_price != []):
                temp = second_price[0].text.replace('总价', ''). \
                                           replace(' ', '').replace('万/套起', '')
                if temp.isdigit():
                    item['second_price'] = int(temp)
                else:
                    item['second_price'] = temp
            else:
                item['second_price'] = NOT_EXIST
            temp = li.find_all(attrs={'class': 'resblock-tag'})
            if temp:
                tag = temp[0].text.replace('', '').split('\n')
                item['tag'] = tag[1:-1]
            else:
                item['tag'] = []
            item['crawl_time'] = int(time.time())
            yield item
