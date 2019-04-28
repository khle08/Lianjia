# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ErshoufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # name = scrapy.Field()
    city = scrapy.Field()
    house_url = scrapy.Field()
    img_url = scrapy.Field()
    title = scrapy.Field()
    xiaoqu_url = scrapy.Field()
    xiaoqu_name = scrapy.Field()
    huxing = scrapy.Field()
    position_info = scrapy.Field()
    position = scrapy.Field()
    position_url = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    crawl_time = scrapy.Field()
    # follow_info = scrapy.Field()


class NewhouseItem(scrapy.Item):
    loupan = scrapy.Field()
    loupan_url = scrapy.Field()
    wuye_type = scrapy.Field()
    sale_status = scrapy.Field()
    img_url = scrapy.Field()
    location = scrapy.Field()
    huxing = scrapy.Field()
    area = scrapy.Field()
    main_price = scrapy.Field()
    main_price_desc = scrapy.Field()
    second_price = scrapy.Field()
    tag = scrapy.Field()
    crawl_time = scrapy.Field()

