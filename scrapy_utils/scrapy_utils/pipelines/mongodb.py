from pymongo import MongoClient
from twisted.internet.threads import deferToThread


class MongoDBPipeline(object):
    def __init__(self, database, name_spaces):
        self.database = database
        self.name_spaces = name_spaces

    @classmethod
    def from_settings(cls, settings):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        user = settings["MONGODB_USER"]
        password = settings["MONGODB_PASSWORD"]
        db_name = settings["MONGODB_DATABASE"]
        name_spaces = settings["MONGODB_TABLE"]
        if not user and not password:
            client = MongoClient(host=host, port=port)
        else:
            client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}/')
        database = client[db_name]
        return cls(database, name_spaces)

    def _process_item(self, item, spider):
        if hasattr(spider, 'spider_mongodb_table'):
            self.database[spider.spider_mongodb_table].insert_one(item)
        else:
            self.database[self.name_spaces].insert_one(item)
        return item

    def process_item(self, item, spider):
        return deferToThread(self._process_item, item, spider)
