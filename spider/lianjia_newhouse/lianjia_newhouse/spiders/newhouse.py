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
            item['loupan'] = li.find_all(attrs={'class': 'name'})[0].text
            item['city'] = self.city
            item['loupan_url'] = self.city_url[:-1] + li.find_all(attrs={'class': 'name'})[0].attrs['href']
            item['wuye_type'] = li.find_all(attrs={'class': 'resblock-type'})[0].text
            item['sale_status'] = li.find_all(attrs={'class': 'sale-status'})[0].text
            item['img_url'] = li.find_all(attrs={'class': 'lj-lazy'})[0].attrs['data-original']
            item['location'] = li.find_all(attrs={'class': 'resblock-location'})[0].text.replace('\n', '').split('/')
            item['huxing'] = li.find_all(attrs={'class': 'resblock-room'})[0].text.replace('\n', '')
            tmp_area = li.find_all(attrs={'class': 'resblock-area'})[0].text. \
                replace(' ', '').replace('\n', '').replace('建面', '').replace('㎡', '')
            if tmp_area == '':
                item['area'] = []
            else:
                list = tmp_area.split('-')
                item['area'] = [int(i) for i in list]
            main_price = li.find_all(attrs={'class': 'number'})
            if (main_price != []):
                item['main_price'] = int(main_price[0].text.replace(' ', ''))
            else:
                item['main_price'] = NOT_EXIST
            main_price_desc = li.find_all(attrs={'class': 'desc'})
            if main_price_desc != []:
                item['main_price_desc'] = main_price_desc[0].text.replace('\xa0','')
            else:
                item['main_price_desc'] = NOT_EXIST
            second_price = li.find_all(attrs={'class': 'second'})
            if (second_price != []):
                item['second_price'] = int(second_price[0].text.replace('总价', ''). \
                                           replace(' ', '').replace('万/套起', ''))
            else:
                item['second_price'] = NOT_EXIST
            tag = li.find_all(attrs={'class': 'resblock-tag'})[0].text.replace('', '').split('\n')
            item['tag'] = tag[1:-1]
            item['crawl_time'] = int(time.time())
            yield item
