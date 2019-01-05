#coding:utf-8


import requests
import time

url = 'https://www.guazi.com/bj/buy/'


#模拟初次请求，不带cookie

from selenium import webdriver


'''
brow = webdriver.Chrome()
try:
    brow.get(url)
    cookie_t = {}
    cookie_t['antipas'] = brow.get_cookie('antipas')['value']
    brow.close()
except:
    print('error')
finally:
    print('done!')
    
'''

'''

# 模拟初次请求，不带cookie，使用chrome headless

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



time1 = time.time()
try:
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--disable-gpu')
    chrome_option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
    browser = webdriver.Chrome(chrome_options=chrome_option)
    browser.get(url)

    #browser.close()
    #browser.quit()

except:
    print('error')
finally:
    time2 = time.time()
    print(time2-time1)

b = browser

cookie_t2 = {}


cookie_t1 = browser.get_cookies()
for i in cookie_t1:
    cookie_t2[i['name']] = i['value']

'''



# 模拟初次请求，不带cookie

header = {
    'Host':'www.guazi.com',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'refer':'https://www.guazi.com/bj/buy/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    }

#req = requests.Request(url,headers=header)


import re
'''
response = requests.get(url,headers=header,verify=False)
print(response.status_code)

c = response.text
'''
'''
import execjs

patt = re.compile("var\svalue=.*?\('(.*?)','(.*?)'\)")

with open('b.txt','r',encoding='utf-8') as fi:
    data = fi.read()

with open('js_code.txt','r',encoding='utf-8') as fi:
    js_code_data = fi.read()
cookie_args = list(re.search(patt, data).groups())
ctx = execjs.compile(js_code_data)
cookie_anti = ctx.call('anti',*cookie_args)
print(cookie_anti)
'''


'''
# 模拟二次请求，带cookie

cookie="""antipas=4232685135j707364014962I1Z; uuid=9b60bc80-0900-456e-83a9-1fbd08ee0f11; cityDomain=bj; clueSourceCode=%2A%2300; ganji_uuid=9858325758580218603351; sessionid=c6c6a719-dde2-4cff-889a-9d48aae35342; lg=1; cainfo=%7B%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_i%22%3A%22-%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%229b60bc80-0900-456e-83a9-1fbd08ee0f11%22%2C%22sessionid%22%3A%22c6c6a719-dde2-4cff-889a-9d48aae35342%22%7D; preTime=%7B%22last%22%3A1542898334%2C%22this%22%3A1542898322%2C%22pre%22%3A1542898322%7D"""
cookie = ""
header = {
    'Host':'www.guazi.com',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'refer':'https://www.guazi.com/bj/buy/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie':cookie
          }
 #'Cookie':cookie
req = requests.Request(url,headers=header)


#response = requests.get(url,headers=header,verify=False)
response = requests.get(url,headers=header,verify=False)
'''






from lxml import etree

'''
# 一级页面提取城市对应url
with open('page_first.txt', 'r', encoding='utf-8') as fi:
    data = fi.read()

page = etree.HTML(data)

citys_t = page.xpath('//div[@class="city-scroll"]//a')

citys_url = {}
for _ in citys_t:
    city_name = _.xpath('text()')[0].strip()
    city_url = _.xpath('@href')
    if isinstance(city_name, str):
        citys_url[city_name] = city_url



cars_list = page.xpath('//li[@data-scroll-track]/a/@href')

'''

'''
# 二级页面解析提取下一页地址

with open('page_2.txt', 'r', encoding='utf-8') as fi:
    data = fi.read()
page = etree.HTML(data)
next_page = page.xpath('//div[@class="pageBox"]//a/@href')[-1]
#print(etree.tostring(next_page))
print(next_page)
'''



'''
# 三级页面解析，提取车辆信息

with open('page_third.txt', 'r', encoding='utf-8') as fi:
    data = fi.read()
page = etree.HTML(data)
item_info = dict()
car_id = page.xpath('//div[@class="right-carnumber"]/text()')[0].split('：')[1].strip()
item_info['id'] = car_id

car_name = page.xpath('//div[@class="product-textbox"]/h2/text()')[0].strip()
item_info['name'] = car_name

car_price = dict()
car_price_t= page.xpath('//div[@class="pricebox js-disprice"]/span/text()')
car_price['建议价格'] = car_price_t[0].strip()
car_price['新车指导价'] = car_price_t[1].strip()
item_info['价格'] = car_price

car_base_jiance = dict()
t = page.xpath('//div[@class="guazi-renzheng"]')[0]
t1 = t.xpath('//div[@class="test-con"]/text()')[0]
car_base_jiance['评估师'] = t1
t2 = t.xpath('//ul[@class="jiance-con  clearfix js-reportTop"]//text()')

car_base_jiance['检测结果'] = list(filter(None,[x.strip() for x in t2]))
t3 = t.xpath('//p[@class="bottom-text"]/text()')
car_base_jiance['检测时间'] = t3
item_info['瓜子检测'] = car_base_jiance

car_base_info = dict()
t = page.xpath('//div[@class="basic-infor js-basic-infor js-top"]')[0]
t1 = t.xpath('.//dl[@class="people-infor clearfix"]//span/text()')
car_base_info['车辆用途简介'] = list(filter(None, [x.strip() for x in t1]))[2:]
t2 = t.xpath('./ul//text()')
car_base_info['车辆信息'] = list(filter(None, [x.strip() for x in t2]))
item_info['车辆基本信息'] = car_base_info

print(item_info)
#c = list(filter(None,car_info_text))
'''



'''

# other

import re

def va(x):
    if 'e' in x:
        return '4444'
    else:
        return '66666'

st = 'a cd ew sdfwe wef wef '

patt = re.compile('\\b\s+\\b')




res = re.sub(patt,va,st)
print(res)



'''

'''
# collections
import collections

class fun():
    def cd(self):
        print('{}'.format(self))

d = collections.defaultdict(fun)
print(d)
a = d[4]
a = d[5]
a = d[7]
print(d)
print(a)
c = fun()
c.cd()
print('www')
for i in d:
    d[i].cd()

'''
'''
# path 拼接

import os

path_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'tt.py'
file_path = os.path.join(path_dir,file_name)
print(path_dir)
print(file_path)

'''

# 引用
'''
from guazi.cookie_provider import cookie_provider

a = cookie_provider.CookiesGet()
'''


from collections import defaultdict

class f():
    pass

a = defaultdict(f)
b = a[1]
c = a['']
d ={4:5}
print(d.get(5))

print(a[d.get(5)])
print(a)
a.popitem()



