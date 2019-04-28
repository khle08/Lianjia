# run scrapy by cmd
from scrapy import cmdline


def run_newhouse():
    args = "scrapy crawl newhouse".split()
    cmdline.execute(args)


if __name__ == '__main__':
    run_newhouse()
