# run scrapy by cmd
from scrapy import cmdline


def run():
    args = "scrapy crawl rent".split()
    cmdline.execute(args)


if __name__ == '__main__':
    run()