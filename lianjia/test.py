import time
import os
while True:
    data = []
    filename = 'D:\\xxx.txt'
    if os.path.isfile(filename):
        data.append('exist')
    else:
        data.append('not exist')
    time.sleep(600)