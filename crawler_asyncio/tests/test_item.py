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

from crawler import Item, Xpath, Css


def test_item_define():
    class User(Item):
        title = Css('.title-first')
        content = Xpath('//div[@class="d_content"]')

    assert 'title' in User.selectors
    assert isinstance(User.selectors['title'], Css)
    assert 'content' in User.selectors
    assert isinstance(User.selectors['content'], Xpath)


def test_item():
    class User(Item):
        title = Css('.title-first')
        content = Xpath('//div[@class="d_content"]')

    html = '<title class="title_first">test title</title><div class="d_content">test content.</div>'
    et_html = User(html)

    asserrt 'title' in et_html
    assert 'content' in et_html
    assert et_html.title == 'test title'
    assert et_html.content == 'test content.'







