import pymongo

map = {}
for i in range(0, 100000, 5000):
    map['{}-{}'.format(i, i + 5000)] = {
        '$gte': i,
        '$lt': i + 5000
    }
for key,value in map.items():
    print(key)
    print(value)
