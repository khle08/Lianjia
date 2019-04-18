import random
import re
from bs4 import BeautifulSoup
from Anjuke.init import *
from Anjuke.getCityPinyin import CityPinyin
import requests


def getPerPageErshoufang(html):
    soup = BeautifulSoup(html,'lxml')
    house_title = []
    details = []
    temp_detail = []
    brokername = []
    address = []
    data = soup.find_all(class_='houseListTitle')
    for d in data:
        house_title.append(d.text.replace('\n','').replace(' ',''))
    data = soup.find_all(class_='details-item')
    # print(data)
    for d in data:
        temp = d.text.split('\ue147')
        try:
            details.append(temp[0].replace('\xa0','').replace('\n','').replace(' ',''))
        except:
            details="未知"
        try:
            brokername.append(temp[1].replace(' ',''))
        except:
            brokername.append("未知")
    print(details)
    return html


def getCityErshoufang(city):
    urls = [
        'https://{}.anjuke.com/sale/p{}/#filtersort'.format(CityPinyin(city),i)
        for i in range(1,51)
    ]
    ershoufang = []
    for url in urls:
        response = requests.get(url,headers=header)
        page_data = getPerPageErshoufang(response.text)
        ershoufang.append(page_data)
    return ershoufang



getCityErshoufang('上海')

