# run scrapy by cmd
from scrapy import cmdline


def run_ershoufang():
    args = "scrapy crawl ershoufang".split()
    cmdline.execute(args)


if __name__ == '__main__':
    run_ershoufang()
