#coding:utf-8
"""
生成原始cookie
生成方法是对制定网站进行请求，得到关键参数，按参数运行js脚本，得到初始cookie值

"""

import requests
import execjs
from re import compile, search

import os.path

from selenium import webdriver

from guazi.settings import DEFAULT_REQUEST_HEADERS
from guazi.settings_o import START_URL_O

import logging


class CookiesGet():
    """
    获取cookie
    """
    _js_env = None

    def __init__(self):
        self._js_env_set()
        pass

    def _js_env_set(self):
        path_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = 'js_code.txt'
        file_path = os.path.join(path_dir,file_name)
        with open(file_path, 'r', encoding='utf-8') as fi:
            js_code = fi.read()
        self._js_env = execjs.compile(js_code)

    def get_cookies_js(self, url):
        header = DEFAULT_REQUEST_HEADERS
        response = requests.get(url, headers=header, verify=False)
        patt = compile("var\svalue=.*?\('(.*?)','(.*?)'\)")
        anti_args = list(search(patt, response.text).groups())
        value = self._js_env.call('anti', *anti_args)
        name = 'antipas'
        return {name: value}

    # 获取cookie
    @staticmethod
    def get_cookies_selenium(url):
        """
        使用selenium+chrome 获取cookie
        :param url: 网页地址
        :return: cookie
        """
        cookie = {}
        try:
            chrome_option = webdriver.ChromeOptions()
            chrome_option.add_argument('--headless')
            chrome_option.add_argument('--disable-gpu')
            chrome_option.add_argument(
                '--user-agent=Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
            browser = webdriver.Chrome(chrome_options=chrome_option)
            browser.get(url)
            cookie_t1 = browser.get_cookies()
            browser.quit()
            for i in cookie_t1:
                cookie[i['name']] = i['value']
            # cookie_t2['lg'] = '1'
        except Exception:
            print('error')
        if cookie:
            return cookie

    def create_cookies_pool(self, url, num=1):
        cookies_pool = list()
        for _ in range(num):
            cookies_pool.append(self.get_cookies_js(url))
        return cookies_pool



if __name__ == '__main__':
    import sys
    sys.path.append('../../')
    url = START_URL_O
    a = CookiesGet()
    #cookie = a.get_cookies_js(url)
    cookie_pool = a.create_cookies_pool(url, 5)
    print(cookie_pool)
