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

from crawler import Css, Item, Parser, Xpath

def test_parse():
    html = '<title class="title_first">test title</title><div class="d_content">test content.</div>'

    class TestItem(Item):
        title = Css('.title_first')
        content = Xpath('//div/text()')

    parser = Parser(html, TestItem)
    item = parser.parse_item(html)

    expected_result = {
        'title': 'test title',
        'content': 'test content.'
    }
    assert item.results == expected_result,'error!'


test_parse()


