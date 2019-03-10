from pymongo import MongoClient
from pandas import DataFrame
from Anjuke.init import *
from Anjuke.cityList import citylist
from Anjuke.getPerCityNewHouse import getCityHouse

def mongo(house, city):
    douban = MongoClient('localhost', 27017)
    douban_db = douban['anjuke']
    douban_set = douban_db.create_collection(city)
    for per_house in house:
        try:
            douban_set.insert(per_house)
            douban_set.save(per_house)
            print(" 成功存入数据库 ")
        except:
            print("存入数据库失败")
    print("{} 房产数据获取完成".format(city))

def excel(house,city):
    data = {}
    loupan_name =[]
    loupan_address =[]
    price =[]
    loupan_tel =[]
    loupan_img =[]
    detail_url =[]
    sale_status =[]
    wuyetp =[]
    area = []
    huxing = []
    tag = []
    for h in house:
        try:
            loupan_name.append(h['loupan_name'])
        except:
            loupan_name.append("None")
            pass
        try:
            loupan_address.append(h['loupan_address'])
        except:
            loupan_address.append("未知地址")
            pass
        try:
            price.append(h['price'])
        except:
            price.append("未知价格")
            pass
        try:
            loupan_tel.append(h['loupan_tel'])
        except:
            loupan_tel.append("None")
            pass
        try:
            loupan_img.append(h['loupan_img'])
        except:
            loupan_img.append("None")
            pass
        try:
            detail_url.append(h['detail_url'])
        except:
            detail_url.append("未知")
        try:
            if h['sale_status']!='':
                sale_status.append(h['sale_status'])
            else:
                sale_status.append("未知")
        except:
            sale_status.append("未知")
            pass
        try:
            if h['wuyetp']!='':
                wuyetp.append(h['wuyetp'])
            else:
                wuyetp.append("未知")
        except:
            wuyetp.append("未知")
            pass
        try:
            if h['area']!='':
                area.append(h['area'])
            else:
                area.append("未知")
        except:
            area.append("未知")
            pass
        try:
            if h['huxing']!='':
                huxing.append(h['huxing'])
            else:
                huxing.append("未知")
        except:
            huxing.append("未知")
            pass
        try:
            if h['tag']!='':
                tag.append(h['tag'])
            else:
                tag.append("未知")
        except:
            tag.append("未知")
            pass
    data['loupan_name'] = loupan_name
    data['loupan_address'] = loupan_address
    data['price'] = price
    data['loupan_tel']=loupan_tel
    data['loupan_img']=loupan_img
    data['detail_url']=detail_url
    data['sale_status']=sale_status
    data['wuyetp'] = wuyetp
    data['loupan_area'] = area
    data['huxing'] = huxing
    data['tag'] = tag
    for key,value in data.items():
        print(key)
        print(value)
    frame = DataFrame(data)
    frame.to_excel(datapath+"\\newhouse_excel"+"\\"+city+".xls",index=True)
    print("{} 成功存入excel".format(city))
    frame.to_json(datapath+"\\newhouse_json"+"\\"+city+".json",index=True)
    print("{} 成功存入json".format(city))
    # frame.to_html(datapath+"\\html"+"\\"+city+".html",index=True)
    # print("{} 成功存入html".format(city))


def china_total_newhouse(china_city,china_num):
    china_house['city'] = china_city
    china_house['num'] = china_num
    frame = DataFrame(china_house)
    frame.to_excel(datapath+"\\china_newhouse_anjuke.xls",index=True)

def parse_newhouse():
    all_city = citylist()
    dir = os.listdir("D:\Anjuke\\newhouse_excel")
    data = []
    for i in dir:
        data.append(i.replace('.xls', ''))
    for key ,value in all_city.items():
        if key in data:
            break
        else:
            house = getCityHouse(key)
            mongo(house,key)
            excel(house,key)
    china_total_newhouse(china_city,china_num)
parse_newhouse()
