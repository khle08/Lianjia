import requests
import re
from Lianjia.init import *
import json
def citylist():
    url = 'https://www.lianjia.com/city/'
    list = re.findall(re.compile('<li><a href="https://(.+?).lianjia.com/">(.+?)</a></li>'),
                      requests.get(url, headers=header).text)
    all_city = {}
    for item in list:
        all_city[item[1]] = "https://{}.lianjia.com/".format(item[0])
    return all_city

def getlianjia():
    url = 'https://nt.fang.lianjia.com/loupan/pg1/?_t=1'
    list = requests.get(url,headers = header).text
    data = json.loads(list)['data']
    for key,value in data.items():
        print(key)
        print(value)
getlianjia()