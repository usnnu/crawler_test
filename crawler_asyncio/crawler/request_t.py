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

import asyncio
from crawler.mylogger import mylogger

logger = mylogger(__name__).logger


async def fetch(url, spider, session, semphore):
    with (await semphore):
        try:
            if callable(spider.headers):
                headers = spider.headers()
            else:
                headers = spider.headers
            async with session.get(url, headers=headers, proxy=spider.proxy) as response:
                if response.status in (200, 201):
                    data = await response.text()
                    return data
                logger.error('Error:{} {}'.format(url, response.status))
                return None
        except:
            return None
