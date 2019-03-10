from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import re
from bs4 import BeautifulSoup
from Anjuke.init import *
from Anjuke.getCityPinyin import CityPinyin
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent={}'.format(random.choice(useragent)))
options.add_argument('cookies={}'.format(random.choice(cookies)))
browser = webdriver.Chrome(chrome_options=options)


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
    url = 'https://{}.anjuke.com/sale/'.format(CityPinyin(city))
    browser.get(url)
    ershoufang = []
    for i in getPerPageErshoufang(browser.page_source):
        ershoufang.append(i)
    while True:
        try:
            browser.find_element_by_class_name('aNxt').click()
            print("正在获取 {}".format(browser.current_url))
            for i in getPerPageErshoufang(browser.page_source):
                ershoufang.append(i)
        except NoSuchElementException:
            print("{} 页面获取完成".format(city))
            break


getCityErshoufang('上海')

