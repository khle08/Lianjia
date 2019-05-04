import requests
from lianjia.constants import *
import time
import json


def es_search(type, keyword):
    map = {1: 'all', 2: 'ershoufang', 3: 'newhouse', 4: 'rent'}
    type = map[type]
    indices = []
    result = []
    indices.append('lianjia_newhouse' +
                   str(time.strftime('%Y%m%d', time.localtime(time.time()))))
    indices.append('lianjia_rent' +
                   str(time.strftime('%Y%m%d', time.localtime(time.time()))))
    indices.append('lianjia_ershoufang' +
                   str(time.strftime('%Y%m%d', time.localtime(time.time()))))
    if type == 'all':
        for i in indices:
            response = requests.get('http://localhost:9200/{}/_search?q={}'.format(i, keyword)).text
            data = json.loads(response)
            if 'hits' in data.keys():
                data = data['hits']
                if 'hits' in data.keys():
                    result.extend(data['hits'])
        return process_data(result)
    else:
        indice = 'lianjia_{}'.format(type) + str(time.strftime('%Y%m%d', time.localtime(time.time())))
        response = requests.get('http://localhost:9200/{}/_search?q={}'.format(indice, keyword)).text
        data = json.loads(response)
        if 'hits' in data.keys():
            data = data['hits']
            if 'hits' in data.keys():
                result.extend(data['hits'])
        return process_data(result)


def process_data(data):
    newhouse = []
    rent = []
    ershoufang = []
    for i in data:
        i['_source']['crawl_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['_source']['crawl_time']))
        if i['_type'] == 'newhouse':
            newhouse.append(i['_source'])
        if i['_type'] == 'ershoufang':
            ershoufang.append(i['_source'])
        if i['_type'] == 'rent':
            rent.append(i['_source'])
    return {
        'newhouse': newhouse,
        'ershoufang': ershoufang,
        'rent': rent
    }
