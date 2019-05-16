import requests
import json
header = {
    'Cookie': 'stra=15031210101; JSESSIONID=C174419866BEC6DC342B12D9EB0A1022',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.96 Safari/537.36'
}
response = requests.get('http://gp.ayit.edu.cn/dataGrid!d0157Treegrid.action?stra=0306&strb=2019&strc=',
                        headers=header).text
data = json.loads(response)
for key,value in data.items():
    # print(key)
    print(value)