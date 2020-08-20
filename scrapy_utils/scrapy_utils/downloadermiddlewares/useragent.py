import logging
import random
from scrapy_utils.utils.useragentlist import USER_AGENT_LIST


class UseragentMiddleware(object):
    def __init__(self, user_agent):
        self.logger = logging.getLogger(__name__)
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent)
        request.headers[b'User-Agent'] = ua

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        user_agent_list = settings.get('USER_AGENT_LIST')
        user_agent_list = user_agent_list if user_agent_list else USER_AGENT_LIST
        return cls(user_agent=user_agent_list)
