import requests
import random
def rand_data():
    url = 'http://localhost:5601/api/console/proxy?path=%2Fngfw%2Fsecurity%2F2&method=PUT'
    data = {
        "src_type" :  random.randint(1,50),
        "dst_type" :   random.randint(1,60),
        "dst_ip" :  "{}.{}.{}.{}".format(random.randint(1,255),
     random.randint(1, 255),random.randint(1,255),random.randint(1,255)),
        "src_ip":       "{}.{}.{}.{}".format(random.randint(1,255),
     random.randint(1, 255),random.randint(1,255),random.randint(1,255)),
        "rule_minor_type": random.randint(1,20),
        "rule_major_type" : random.randint(1,30),
        "group" : random.randint(1,90),
        "branch_id" : random.randint(1,50),
        "level":random.randint(1,11),
        "country_crc": random.randint(100000,999999),
        "province_crc": random.randint(100000,999999),
        "attack_type" : random.randint(1,30),
        "module_type" : random.randint(1,30),
        "rule_id" : random.randint(1000,99999)
    }
    print(data)
for i in range(100):
    rand_data()