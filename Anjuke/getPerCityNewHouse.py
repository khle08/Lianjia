import re
import requests
from functools import reduce
from bs4 import BeautifulSoup
from Anjuke.getCityPinyin import CityPinyin
from Anjuke.init import *



def getCityPageNum(city):
    response = requests.get("https://{}.fang.anjuke.com/".format(CityPinyin(city)), headers=header)
    total = 1
    try:
        total = int(re.findall(re.compile(r'<span class="total">共有<em>(.+?)</em>.*?楼盘</span>'), response.text)[0])
    except:
        total = 1
    print("{} 一共有{} 页".format(city,int(total/60+1)))
    return int(total/60+1)


def getPageData(pageurl):
    print("crawling {}".format(pageurl))
    response = requests.get(pageurl, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    page_house_list = []
    house = {}
    loupan_name = re.findall(re.compile('<span class="items-name">(.+?)</span>'), response.text)
    loupan_address = re.findall(re.compile('<span class="list-map" target="_blank">(.*?)</span>'), response.text)
    loupan_address = [i.replace('&nbsp;', '') for i in loupan_address]
    html = soup.find_all(class_='price')
    price = [p.text for p in html]
    loupan_tel = re.findall(re.compile('<p class="tel">(.+?)</p>'), response.text)
    loupan_tel = [i.replace('<i class="iconfont tel-icon">&#xeb12;</i>', '') for i in loupan_tel]
    loupan_img = re.findall(re.compile(r'<img width="180" height="135" src="(.+?)" alt="">'), response.text)
    detail_url = re.findall(re.compile(r'data-link="(.+?)"'), response.text)
    huxing = []
    area = []
    sale_status = []
    wuyetp = []
    tag = []
    datas = soup.find_all(class_='tag-panel')
    for data in datas:
        temp = data.text.split('\n')
        sale_status.append(temp[1])
        wuyetp.append(temp[2])
        tag.append(' '.join(temp[3:-1]))
    datas = soup.find_all(class_='huxing')
    for data in datas:
        text = data.text.replace('\t', '').replace('\n', '').replace(' ',
        '').replace('\xa0', '').split('建筑面积：')
        huxing.append(text[0].split(':')[0].replace('户型：', ''))
        area.append(text[1])
    for i in range(len(loupan_name)):
        try:
            house['loupan_name'] = loupan_name[i]
        except IndexError:
            house['loupan_name'] = 'None'
            print("loupan_name IndexError")
            pass
        try:
            house['loupan_address'] = loupan_address[i]
        except IndexError:
            house['loupan_address'] = "未知地址"
            print("loupan_address IndexError")
            pass
        try:
            house['price'] = price[i]
        except IndexError:
            house['price'] = '售价待定'
            print("price IndexError")
            pass
        try:
            house['loupan_tel'] = loupan_tel[i]
        except IndexError:
            house['loupan_tel'] = '暂无电话'
            print('loupan_tel IndexError')
            pass
        try:
            house['loupan_img'] = loupan_img[i]
        except IndexError:
            house['loupan_img'] = "None"
            print("loupan_img IndexError")
            pass
        try:
            house['detail_url'] = detail_url[i]
        except IndexError:
            house['detail_url'] = "error"
            print("detail_url IndexError")
            pass
        try:
            house['sale_status'] = sale_status[i]
        except IndexError:
            house['sale_status'] = "未知"
            print("sale_status IndexError")
        try:
            house['wuyetp'] = wuyetp[i]
        except IndexError:
            house['wuyetp'] = '未知'
            print("wuyetp IndexError")
            pass
        try:
            house['area'] = area[i]
        except IndexError:
            house['area'] = '未知'
            print("area IndexError")
            pass
        try:
            house['tag'] = tag[i]
        except IndexError:
            house['tag'] = '未知'
            print("tag IndexError")
            pass
        try:
            house['huxing'] = huxing[i]
        except IndexError:
            house['huxing'] = '未知'
            print("huxing IndexError")
            pass
        page_house_list.append(house)
        house = {}
    return page_house_list

# get house
def getCityHouse(city):
    print("正在获取 {}".format(city))
    total_page = getCityPageNum(city)
    city_house = []
    for i in range(1,total_page+1):
        data = getPageData('https://{}.fang.anjuke.com/loupan/all/p{}/'.format(CityPinyin(city),i))
        for i in data:
            city_house.append(i)
    # 去重
    run_function = lambda x, y: x if y in x else x + [y]
    city_house = reduce(run_function, [[], ] + city_house)
    print("{}一共{}个售房信息".format(city,len(city_house)))
    china_city.append(city)
    china_num.append(len(city_house))
    return city_house

