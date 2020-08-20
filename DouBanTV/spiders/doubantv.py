# -*- coding: utf-8 -*-

import scrapy
import json
from DouBanTV.utils.util import get_md5


class DoubantvSpider(scrapy.Spider):
    name = 'doubantv'
    allowed_domains = ['douban.com']
    tv_type = ["热门", "美剧", "英剧", "韩剧", "日剧", "国产剧", "港剧", "日本动画", "综艺", "纪录片"]
    start_urls = [
        f'https://movie.douban.com/j/search_subjects?type=tv&tag={i}&sort=recommend&page_limit=20&page_start=0' for i in
        tv_type]

    spider_mongodb_table = None
    spider_mysql_table = None

    def parse(self, response, **kwargs):
        json_data = json.loads(response.text).get("subjects")
        if not json_data:
            return None
        for data in json_data:
            item = {}
            item['rate'] = data.get('rate')
            item['title'] = data.get('title')
            item['url'] = data.get('url')
            item['cover'] = get_md5(data.get('cover'))
            item['id'] = data.get('id')
            yield item

            # yield scrapy.Request(url=item['url'], callback=self.test1, dont_filter=False)

        url = response.url
        page_start_str = url[url.rindex("page_start="):]
        current_numb = int(page_start_str[11:])
        next_page = url.replace(page_start_str, f"page_start={current_numb + 20}")
        yield scrapy.Request(url=next_page, callback=self.parse, dont_filter=False)

    def test1(self, response):
        print(response.url)


if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute(["scrapy", "crawl", "doubantv"])
