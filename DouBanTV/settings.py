# -*- coding: utf-8 -*-

# Scrapy settings for DouBanTV project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DouBanTV'

SPIDER_MODULES = ['DouBanTV.spiders']
NEWSPIDER_MODULE = 'DouBanTV.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'DouBanTV (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'DouBanTV.middlewares.DoubantvSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'DouBanTV.middlewares.DoubantvDownloaderMiddleware': 543,
    "scrapy_utils.downloadermiddlewares.useragent.UseragentMiddleware": 200,
    # "scrapy_utils.downloadermiddlewares.proxy_adsl.ProxyAdslMiddleware": 201

}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # "scrapy_utils.pipelines.mongodb.MongoDBPipeline": 203,
    # "scrapy_utils.pipelines.mysql.MysqlTwistedPipeline": 203

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "147963"
MYSQL_DATABASE = "test1"
MYSQL_TABLE = "test_1"

MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_USER = None
MONGODB_PASSWORD = None
MONGODB_DATABASE = "test"
MONGODB_TABLE = "test_db"

# 使用的哈希函数数，默认为6
BLOOMFILTER_HASH_NUMBER = 6
# Bloomfilter使用的Redis内存位，30表示2 ^ 30 = 128MB，默认为22 (1MB 可去重130W URL)
BLOOMFILTER_BIT = 22
# 不清空redis队列 （默认为True）
SCHEDULER_PERSIST = True
# 调度队列
SCHEDULER = "scrapy_utils.scrapy_redis_bc.scheduler.Scheduler"
# 去重（默认配好）
# DUPEFILTER_CLASS = "scrapy_utils.scrapy_redis_bc.dupefilter.RFPDupeFilter"
# queue（默认配好）
# SCHEDULER_QUEUE_CLASS = "scrapy_utils.scrapy_redis_bc.queue.PriorityQueue"
# redis单机
REDIS_URL = 'redis://127.0.0.1:6379/1'
# redis集群
# REDIS_MASTER_NODES = [
#     {"host": "127.0.0.1", "port": "30001"},
#     {"host": "127.0.0.2", "port": "30002"},
#     {"host": "127.0.0.13", "port": "30003"},
# ]
