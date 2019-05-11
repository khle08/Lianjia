from data_visualize.newhouse import newhouse
from data_visualize.ershoufang import ershoufang
from data_visualize.rent import rent
import threading

if __name__ == '__main__':
    one = threading.Thread(target=ershoufang())
    one.start()
    two = threading.Thread(target=newhouse())
    two.start()
    three = threading.Thread(target=rent())
    three.start()