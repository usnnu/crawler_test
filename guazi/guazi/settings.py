# -*- coding: utf-8 -*-

# Scrapy settings for guazi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'guazi'

SPIDER_MODULES = ['guazi.spiders']
NEWSPIDER_MODULE = 'guazi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'guazi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'guazi.middlewares.GuaziSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'guazi.middlewares.GuaziDownloaderMiddleware': 543,
#}

DOWNLOADER_MIDDLEWARES = {
    # 禁用scrapy自带的cookie中间件
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    # 启用自己写的cookie中间件，权重参考scrapy设为700
    'guazi.cookies.CookiesMiddleware': 700,
    'guazi.middlewares.GuaziDownloaderMiddleware': 543,
}


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'guazi.pipelines.GuaziPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



#EXTENSIONS = {
#    'sina.spider_open_s.spider_open': 0
#    }




# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.9',
          'Host':'www.guazi.com',
          'Upgrade-Insecure-Requests':'1',
          'Referer': 'https://www.guazi.com/bj/buy/',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'

                           
          }


#使用scrapy_redis自己的去重处理器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#使用scrapy_redis自己调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#爬虫可以暂停/开始， 从爬过的位置接着爬取
SCHEDULER_PERSIST = True

#不设置的话，默认使用的是SpiderPriorityQueue
#优先级队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

#普通队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#栈
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
   'guazi.pipelines.GuaziPipeline': 301,
   # 把数据默认添加到redis数据库中
   'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 日志级别
LOG_LEVEL = 'WARNING'
#LOG_LEVEL = 'DEBUG'
LOG_FILE = 'log_file.log'


#配置redis数据库信息
#redis端口

#REDIS_URL = 'redis://:123@127.0.0.1:6379/0'
#REDIS_URL = 'redis://192.168.199.129:6379/0'
REDIS_URL = 'redis://:123@192.168.199.113:6379/3'

#下载延迟1秒
#DOWNLOAD_DELAY = 1






# cookie settings
COOKIES_ENABLED = True
#COOKIES_DEBUG = True


# 并发数
CONCURRENT_REQUESTS = 5

