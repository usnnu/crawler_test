#coding:utf-8

from scrapy.cmdline import execute
from os.path import exists
from os import mkdir
from os import chdir


def start_crawler():
    if not exists('download'):
        mkdir('download')
    chdir('download')

    execute("scrapy crawl car_buy_info".split())




if __name__ == "__main__":
    start_crawler()

