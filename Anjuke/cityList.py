import requests
import re
from anjuke.init import *

def citylist():
    all_city = {}
    response = requests.get('https://www.anjuke.com/sy-city.html',headers = header)
    if response.status_code!=200:
        print("网站拒绝响应")

    data = re.findall(re.compile(r'<a href="https://(\w+).anjuke.com">(.+?)</a>'),response.text)
    pinyin = []
    city = []
    for c in data:
        pinyin.append(c[0])
        city.append(c[1])
    for c in data:
        if not c[1] in pinyin:
            temp = c[1]
            if temp[-3:]=='房产网':
                temp = temp[:-3]
            all_city[temp] = c[0]
    print("成功获取 {} ".format(len(all_city)))
    return all_city
citylist()