#coding:utf-8

"""
----------------------------------------
description:
author: sss
date:
----------------------------------------
change:
    
----------------------------------------

"""

__author__ = 'sss'


from crawler import Spider, Item, Parser, Css, Xpath, XpathParser

class Post(Item):
    title = Xpath('//div[@class="d_title"]//text()')
    content = Xpath('//div[@class="hm-scroll"]/text()')

    async def save(self):
        with open('scrapyinghub.txt', 'a+') as fi:
            fi.write(str(self.results)+'\n')

class mySpider(Spider):
    concurrency = 5
    headers = {'User-Agent': 'Google Spider'}
    start_url = 'https://blog.scrapinghub.com/'
    #start_url = ''
    parsers = [Parser('https://blog.scrapinghub.com/page/\d+/'),
               Parser('https://blog.scrapinghub.com/\d{4}/\d{2}/\d{2}/[a-z0-9\-]+/', Post)]

    parsers = [XpathParser('//div[@class="next_page"]'),
               XpathParser('.//dt/a/@href', Post)]

mySpider.run()


