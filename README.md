# ScrapyUtils

### 简介

scrapy各种扩展插件

### Install

```python
ScrapyUtils/scrapy_utils  setup.py
对应的python环境下
python setup.py install
```

### 功能介绍

- DownLoaderMiddlewares

  - useragent

    ```python
    可配置式UserAgentList
    DOWNLOADER_MIDDLEWARES = {
        "scrapy_utils.downloadermiddlewares.useragent.UseragentMiddleware": 200
    }
    可选配置： USER_AGENT_LIST = ['xxxxx'， 'xxxxx'] 不配置为默认UserAgentList
    ```

  - proxy_adsl

    ```python
    Adsl拨号代理
    DOWNLOADER_MIDDLEWARES = {
        "scrapy_utils.downloadermiddlewares.proxy_adsl.ProxyAdslMiddleware": 201
    }
    ADSL_SCRIPT_PATH = "Adsl拨号脚本路径"
CHANGE_VALUE_TIME = 切换时间/秒 (defalut=60)
    ```
    

- Pipelines

  - mongodb

    ```python
    Mongodb异步存储(数据与集合不需要先建好)
    ITEM_PIPELINES = {
        "scrapy_utils.pipelines.mongodb.MongoDBPipeline": 203
    }
    MONGODB_HOST = "127.0.0.1"
    MONGODB_PORT = 27017
    MONGODB_USER = None
    MONGODB_PASSWORD = None
    MONGODB_DATABASE = "test"
    MONGODB_TABLE = "test_db"
    可选配置: 
    不同spider对应不同table可在各spider文件下添加类属性，例如：
    name = 'doubantv'
    allowed_domains = ['douban.com']
    spider_mongodb_table = "XXXX"
    ```

  - mysql

    ```python
    Mysql异步存储(需要先建立好数据库与表,与scrapy item对应)
    ITEM_PIPELINES = {
        "scrapy_utils.pipelines.mysql.MysqlTwistedPipeline": 204
    }
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "147963"
    MYSQL_DATABASE = "test"
    MYSQL_TABLE = "test_db"
    可选配置: 
    不同spider对应不同table可在各spider文件下添加类属性，例如：
    name = 'doubantv'
    allowed_domains = ['douban.com']
    spider_mysql_table = "XXXX"
    ```

- ScrapyRedisBc

  - scrapy_redis_bc

    ```
    scrapy redis Bloom Filter cluster
    scrapy_redis集群布隆过滤器去重
    # 调度队列（必选）
    SCHEDULER = "scrapy_utils.scrapy_redis_bc.scheduler.Scheduler"
    # 去重（可选 默认配好）
    # DUPEFILTER_CLASS = "scrapy_utils.scrapy_redis_bc.dupefilter.RFPDupeFilter"
    # queue（可选 默认配好）
    # SCHEDULER_QUEUE_CLASS = "scrapy_utils.scrapy_redis_bc.queue.PriorityQueue"
    # 使用的哈希函数数 (可选 默认为6)
    BLOOMFILTER_HASH_NUMBER = 6 
    # BIT (可选 默认为22)
    BLOOMFILTER_BIT = 22
    # 不清空redis队列 （可选 默认为True）
    SCHEDULER_PERSIST = True
    # redis单机连接方式
    REDIS_URL = 'redis://127.0.0.1:6379/1'
    # redis集群连接方式
    # REDIS_MASTER_NODES = [
    #     {"host": "127.0.0.1", "port": "30001"},
    #     {"host": "127.0.0.2", "port": "30002"},
    #     {"host": "127.0.0.3", "port": "30003"},
    # ]
    
    ```

    

  

