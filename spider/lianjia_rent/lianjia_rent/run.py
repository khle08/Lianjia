# run scrapy by cmd
from scrapy import cmdline


def run_rent():
    args = "scrapy crawl rent".split()
    cmdline.execute(args)


if __name__ == '__main__':
    run_rent()
