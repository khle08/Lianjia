import os
import random
import datetime

useragent = [
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    ]
cookies = [
    'all-lj=3d8def84426f51ac8062bdea518a8717; lianjia_ssid=af012c30-5b7a-414b-b12b-6d67be77e19a; lianjia_uuid=60768cd4-5897-47e9-83db-d0518431cc0f; select_city=440300',
    'lianjia_ssid=af012c30-5b7a-414b-b12b-6d67be77e19a; lianjia_uuid=60768cd4-5897-47e9-83db-d0518431cc0f; select_city=360800; TY_SESSION_ID=41a5e851-de3b-4fd5-831a-13c055a5bad3; all-lj=762328e22710c88ff41f391dedabbc6f',
    ]
header = {
    'referer': 'https://baidu.com/',
    'user-agent': random.choice(useragent),
    'cookie': random.choice(cookies)
}
china_house = {}
china_city = []
china_num = []
list = [datetime.datetime.now().year, datetime.datetime.now().month,
        datetime.datetime.now().day, datetime.datetime.now().hour,
        datetime.datetime.now().minute, datetime.datetime.now().second]
time = ''
for i in list:
    time += str(i)
datapath = "D:\\Anjuke"
