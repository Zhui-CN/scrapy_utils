import re
import time
import logging
import os
from subprocess import getstatusoutput


class ProxyAdslMiddleware(object):

    def __init__(self, frequency, script_path):
        self.logger = logging.getLogger(__name__)
        self.timestamp = int(time.time())
        self.frequency = frequency
        self.script_path = script_path
        self.proxy = []

    def change_ip(self):
        status, result = getstatusoutput('bash {}'.format(self.script_path))
        if status == 0:
            ip = re.search('inet (.*?) peer', result).group(1)
            if ip in self.proxy:
                return self.change_ip()
            else:
                self.proxy.append(ip)
                self.logger.debug(f'更换IP成功：{ip}')
                return True
        else:
            return False

    def process_request(self, request, spider):
        if int(time.time()) >= self.timestamp + self.frequency:
            if self.change_ip():
                self.timestamp = int(time.time())
            else:
                return request
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        self.logger.debug('网络异常，尝试更换IP')
        self.change_ip()
        self.timestamp = int(time.time())
        return request

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        script_path = settings.get('ADSL_SCRIPT_PATH')
        frequency = settings.get('CHANGE_VALUE_TIME', 60)
        assert script_path
        assert os.path.exists(script_path)
        return cls(frequency=frequency, script_path=script_path)
