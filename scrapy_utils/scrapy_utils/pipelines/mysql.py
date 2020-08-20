from twisted.enterprise import adbapi

try:
    import MySQLdb
    mysql = "MySQLdb"
except:
    import pymysql
    mysql = "pymysql"


class MysqlTwistedPipeline(object):
    def __init__(self, dbpool, table_name):
        self.dbpool = dbpool
        self.table_name = table_name

    @classmethod
    def from_settings(cls, settings):
        db_parms = dict(
            host=settings["MYSQL_HOST"],
            port=settings.get('MYSQL_PORT'),
            user=settings["MYSQL_USER"],
            password=settings["MYSQL_PASSWORD"],
            database=settings["MYSQL_DATABASE"],
            charset='utf8mb4'
        )
        table_name = settings.get('MYSQL_TABLE')
        dbpool = adbapi.ConnectionPool(mysql, **db_parms)
        return cls(dbpool, table_name)

    def close_spider(self, spider):
        self.dbpool.close()

    def _process_item(self, cursor, item, spider):
        if hasattr(spider, 'spider_mysql_table'):
            table = spider.spider_mysql_table
        else:
            table = self.table_name
        keys = ', '.join(item.keys())
        values = ', '.join(['%s'] * len(item))
        sql = 'insert into %s (%s) values (%s)' % (table, keys, values)
        cursor.execute(sql, tuple(item.values()))
        return item

    def process_item(self, item, spider):
        db = self.dbpool.runInteraction(self._process_item, item, spider)
        db.addErrback(self.handle_error, item, spider)
        return item

    @staticmethod
    def handle_error(failure, item, spider):
        print(str(failure))
