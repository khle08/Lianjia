# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import elasticsearch
import pymongo

class ElasticsearchPipeline(object):
    def __init__(self, es_index):
        self.es = elasticsearch.Elasticsearch()
        self.es_index = es_index
        self.es_id = 1

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            es_index=crawler.settings.get('ES_ERSHOUFANG', 'items')
        )

    def open_spider(self, spider):
        try:
            result = self.es.indices.create(index=self.es_index, ignore=400)
            print(result)
        except Exception:
            pass

    def process_item(self, item, spider):
        result = self.es.create(index=self.es_index, doc_type='ershoufang', id=self.es_id, body=dict(item))
        self.es_id += 1
        print(result)
        return item


class LianjiaPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print(item['city'])
        self.db[item['city']].insert_one(dict(item))
        return item
