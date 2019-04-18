import os
import random
import datetime


useragent = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
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
cookies = [    'isp=true; aQQ_ajkguid=5DC9E755-5D55-AAA6-3C8F-48DE23E5DF73; _ga=GA1.2.472502836.1545702982; 58tj_uuid=6b5e6687-8fca-4f2a-8d54-6de63da4e93f; als=0; isp=true; isp=true; sessid=BDD27F4C-4702-1A7B-B085-SX0212164614; new_uv=13; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1547457388,1548895169,1549961178; lps=http%3A%2F%2Fuser.anjuke.com%2Fajax%2FcheckMenu%2F%3Fr%3D0.4067429759969181%26callback%3DjQuery111309305915671582332_1549961177089%26_%3D1549961177090%7Chttps%3A%2F%2Fmsh.fang.anjuke.com%2Floupan%2Fall%2Fp1%2F; twe=2; ctid=60; lp_lt_ut=b3c453662027d1c53102a51504895803; ved_loupans=412038; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1549963026',
               'isp=true; aQQ_ajkguid=97D1D743-EEE8-2563-2052-2EEBB4FB4373; 58tj_uuid=8b16282d-3f5a-43d3-9147-7ed3adc74223; als=0; isp=true; lp_lt_ut=e3f1279980bef66442aa06898ae1c5ac; sessid=B8023EA5-753E-5975-A5EB-60412F2BA6DC; lps=http%3A%2F%2Fluoyang.anjuke.com%2Fsale%2Fp49%2F%7C; twe=2; init_refer=; new_uv=2; new_session=0; propertys=pveboa-pmuncu_; ajk_member_captcha=db558f04fd50a6c917eef120c0e54fe9; ctid=258; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1550029209,1550040659; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1550040665',
               'isp=true; aQQ_ajkguid=5DC9E755-5D55-AAA6-3C8F-48DE23E5DF73; _ga=GA1.2.472502836.1545702982; 58tj_uuid=6b5e6687-8fca-4f2a-8d54-6de63da4e93f; als=0; isp=true; sessid=F52DB6D3-E05A-7CBD-DE03-5BD9C1C398D2; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Ds9QG205y2_afHve2X1UeCBDSE9FNQqhgWt7XSDNDqdyoxIq980FEnzp_B6xWEdTv%26wd%3D%26eqid%3Da47f01240001c8cf000000045c5243a7; twe=2; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1547457388,1548895169; propertys=q01lsx-pm67fz_; ajk_member_captcha=aef3df5e3460c88ba7f600b15f973935; lp_lt_ut=ea25908b4af3ebb5ebae89b9d6663995; init_refer=https%253A%252F%252Fly.fang.anjuke.com%252Floupan%252Fall%252Fp14%252F; new_uv=12; new_session=0; ctid=11; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1549190443']
header = {
            'referer': 'https://baidu.com/',
            'user-agent': random.choice(useragent),
            'cookie': random.choice(cookies)
        }
china_house = {}
china_city = []
china_num = []
list = [datetime.datetime.now().year,datetime.datetime.now().month,
        datetime.datetime.now().day,datetime.datetime.now().hour,
        datetime.datetime.now().minute,datetime.datetime.now().second]
time = ''
for i in list:
    time+=str(i)
datapath = "D:\\Anjuke"

