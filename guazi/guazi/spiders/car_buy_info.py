# -*- coding: utf-8 -*-
import scrapy

from scrapy_redis.spiders import RedisSpider
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TimeoutError, TCPTimedOutError
from guazi.items import GuaziItem

from guazi.utils.mylogger import mylogger
from guazi.settings_o import *
from guazi.settings import DEFAULT_REQUEST_HEADERS


logger_c = mylogger(__name__)
logger_m = logger_c.logger
pages_max_num = 200


class CarBuyInfoSpider(RedisSpider):
    name = 'car_buy_info'
    # allowed_domains = ['guazi.com']
    # start_urls = ['http://guazi.com/']
    redis_key = 'car_buy_info:start_urls'

    def start_requests(self):
        logger_m.info('开始爬取！')
        # self.server.lpush(self.redis_key, start_url_o)
        # 构造请求
        header = DEFAULT_REQUEST_HEADERS
        req = scrapy.Request(url=START_URL_O,
                             headers=header,
                             method='get',
                             callback=self.parse,
                             dont_filter=True)
        return [req]

    # 一级页面解析，获取城市列表
    def parse(self, response):
        if response.status == 203:
            req = response.request
            req.dont_filter = True
            yield req
            return
        logger_m.info('开始解析主目录！')
        page_data = scrapy.Selector(response)
        citys_t = page_data.xpath('//div[@class="city-scroll"]//a')
        citys_url = {}
        for _ in citys_t:
            city_name = _.xpath('text()')[0].extract().strip()
            citys_url[city_name] = _.xpath('@href')[0].extract()

        for i, j in enumerate(citys_url):
            # 测试用
            if j != '北京':
                pass
                continue
            req = scrapy.Request(BASE_URL_O + citys_url[j],
                                 callback=self.parse_second,
                                 meta={'city_name': j},
                                 dont_filter=True,
                                 errback=self._get_error_back)
            yield req

    # 二级页面解析，解析出车辆页面列表，获取车辆详细信息页面地址
    def parse_second(self, response):
        if response.status == 203:
            req = response.request
            req.dont_filter = True
            yield req
            return
        logger_m.info('解析' + response.url)
        page_data = scrapy.Selector(response)
        cars_url_list = page_data.xpath('//li[@data-scroll-track]/a/@href').extract()
        if len(cars_url_list) == 0:
            return None
        for i, j in enumerate(cars_url_list):
            req = scrapy.Request(BASE_URL_O + cars_url_list[i],
                                 callback=self.parse_third,
                                 meta={'city_name': j},
                                 errback=self._get_error_back)
            yield req
        # 下一页地址，构造请求
        next_page = page_data.xpath('//div[@class="pageBox"]//a/@href')[-1].extract()
        if int(next_page.split('/')[-2].strip()[1:]) > 15:
            pass
            # return
        req = scrapy.Request(BASE_URL_O + next_page,
                             callback=self.parse_second,
                             dont_filter=True,
                             errback=self._get_error_back)
        yield req
        pass


    def parse_third(self, response):
        if response.status == 203:
            req = response.request
            yield req
            return
        page = scrapy.Selector(response)
        item = GuaziItem()

        item_info = dict()
        try:
            car_id = page.xpath('.//div[@class="right-carnumber"]/text()')[0].extract().split('：')[1].strip()
            item_info['id'] = car_id

            car_name = page.xpath('//div[@class="product-textbox"]/h2/text()')[0].extract().strip()
            item_info['name'] = car_name

            car_price = dict()
            car_price_t = page.xpath('//div[@class="pricebox js-disprice"]/span/text()').extract()
            car_price['建议价格'] = car_price_t[0].strip()
            car_price['新车指导价'] = car_price_t[1].strip()
            item_info['价格'] = car_price

            car_base_jiance = dict()
            t = page.xpath('//div[@class="guazi-renzheng"]')[0]
            t1 = t.xpath('//div[@class="test-con"]/text()')[0].extract()
            car_base_jiance['评估师'] = t1
            t2 = t.xpath('//ul[@class="jiance-con  clearfix js-reportTop"]//text()').extract()
            car_base_jiance['检测结果'] = list(filter(None, [x.strip() for x in t2]))
            t3 = t.xpath('//p[@class="bottom-text"]/text()').extract()
            car_base_jiance['检测时间'] = t3
            item_info['瓜子检测'] = car_base_jiance

            car_base_info = dict()
            t = page.xpath('//div[@class="basic-infor js-basic-infor js-top"]')[0]
            t1 = t.xpath('.//dl[@class="people-infor clearfix"]//span/text()').extract()
            car_base_info['车辆用途简介'] = list(filter(None, [x.strip() for x in t1]))[2:]
            t2 = t.xpath('./ul//text()').extract()
            car_base_info['车辆信息'] = list(filter(None, [x.strip() for x in t2]))
            item_info['车辆基本信息'] = car_base_info
        except Exception:
            #self.logger.error(response.headers)
            print('except')
            logger_m.error(response)
            logger_m.error(response.text)
            raise Exception

        item['car'] = item_info
        logger_m.info('解析{}'.format(car_id))
        yield item

    def _get_error_back(self, failure):
        logger_m.info('*'*30)
        logger_m.error(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            logger_m.error('HttpError on {}'.format(response.url))

        elif failure.check(DNSLookupError):
            request = failure.request
            logger_m.error('DNSLookupError on {}'.format(request.url))

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            logger_m.error('TimeoutError on {}'.format(request.url))
        else:
            pass
        # logger_m.error()
        logger_m.info('*' * 30)
