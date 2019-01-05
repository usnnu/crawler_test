import os
import six
import logging
from collections import defaultdict

from scrapy.exceptions import NotConfigured
from scrapy.http import Response
from scrapy.http.cookies import CookieJar
from scrapy.utils.python import to_native_str

from guazi.settings_o import *
from guazi.cookie_provider.cookie_provider import CookiesGet


logger = logging.getLogger(__name__)


class CookiesMiddleware(object):
    """This middleware enables working with sites that need cookies
    功能描述：
    1.如果没有可用cookie则调用cookie生成模块生成新cookie
    2.cookie使用指定次数后抛弃
    """

    def __init__(self, debug=False):
        self.jars = defaultdict(CookieJar)
        self.debug = debug
        # 初始cookie池，存放初始cookie
        self.cookies_pool_ori = list()
        # 可用cookiejar的id和已使用次数
        self.cookie_id_useful = list()
        self.cookie_id_cur = 0

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('COOKIES_ENABLED'):
            raise NotConfigured
        return cls(crawler.settings.getbool('COOKIES_DEBUG'))

    def process_request(self, request, spider):
        if request.meta.get('dont_merge_cookies', False):
            return

        if len(self.cookie_id_useful) == 0:
            if len(self.cookies_pool_ori) == 0:
                self._get_new_cookies()
            cookiejarkey = self.cookie_id_cur + 1
            request.cookies = self.cookies_pool_ori.pop()
            times = 0
        else:
            cookiejarkey, times = self.cookie_id_useful.pop(0)
        jar = self.jars[cookiejarkey]
        times += 1
        request.meta['cookiejar'] = [cookiejarkey, times]
        cookies = self._get_request_cookies(jar, request)
        for cookie in cookies:
            jar.set_cookie_if_ok(cookie, request)

        # set Cookie header
        request.headers.pop('Cookie', None)
        jar.add_cookie_header(request)
        self._debug_cookie(request, spider)

    def process_response(self, request, response, spider):
        if request.meta.get('dont_merge_cookies', False):
            return response

        # extract cookies from Set-Cookie and drop invalid/expired cookies
        cookiejarkey, times = request.meta.get("cookiejar")
        # 弃用使用过一定次数的cookie
        if response.status == 203:
            print('cookiejarkey: %d, %d' %(cookiejarkey, times))
            self.jars.pop(cookiejarkey)
            return response

        if times > COOKIE_USE_TIMES:
            self.jars.pop(cookiejarkey)
        else:
            jar = self.jars[cookiejarkey]
            jar.extract_cookies(response, request)
            self._debug_set_cookie(response, spider)
            self.cookie_id_useful.append(request.meta.get('cookiejar'))

        return response

    def _debug_cookie(self, request, spider):
        if self.debug:
            cl = [to_native_str(c, errors='replace')
                  for c in request.headers.getlist('Cookie')]
            if cl:
                cookies = "\n".join("Cookie: {}\n".format(c) for c in cl)
                msg = "Sending cookies to: {}\n{}".format(request, cookies)
                logger.debug(msg, extra={'spider': spider})

    def _debug_set_cookie(self, response, spider):
        if self.debug:
            cl = [to_native_str(c, errors='replace')
                  for c in response.headers.getlist('Set-Cookie')]
            if cl:
                cookies = "\n".join("Set-Cookie: {}\n".format(c) for c in cl)
                msg = "Received cookies from: {}\n{}".format(response, cookies)
                logger.debug(msg, extra={'spider': spider})

    def _format_cookie(self, cookie):
        # build cookie string
        cookie_str = '%s=%s' % (cookie['name'], cookie['value'])

        if cookie.get('path', None):
            cookie_str += '; Path=%s' % cookie['path']
        if cookie.get('domain', None):
            cookie_str += '; Domain=%s' % cookie['domain']

        return cookie_str

    def _get_request_cookies(self, jar, request):
        if isinstance(request.cookies, dict):
            cookie_list = [{'name': k, 'value': v} for k, v in \
                    six.iteritems(request.cookies)]
        else:
            cookie_list = request.cookies

        cookies = [self._format_cookie(x) for x in cookie_list]
        headers = {'Set-Cookie': cookies}
        response = Response(request.url, headers=headers)

        return jar.make_cookies(response, request)

    def _get_new_cookies(self, num=10):
        """
        从原始cookie池中获取初始cookie
        :return:
        """
        self.cookies_pool_ori = CookiesGet().create_cookies_pool(START_URL_O, num)
