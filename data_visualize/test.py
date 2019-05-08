dict = {
    '河南省': 100,
    '湖北省': 120,
    '开发区': 130,
    '文区开发区': 140,
    '郑州市': 150,
    '洛阳市': 160,
    '开封市': 170
}
temp = {}
for key, value in dict.items():
    if key[-3:] == '开发区' and key[-1] == '省':
        dict.pop(key)
print(dict)
