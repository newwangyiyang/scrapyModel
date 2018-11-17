import scrapy
import uuid
import time
from ..items import MysqldemoItem
class MysqlDemo(scrapy.Spider):
    name = 'mysqldemo'
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = ['http://lab.scrapyd.cn/']
    def parse(self, response):
        html_mains = response.css('#main .quote')
        for html_main in html_mains:
            mingyan = html_main.css('.text::text').extract()[0]
            zuoze = html_main.css('.author::text').extract()[0]
            ctime = time.strftime('%Y-%m-%d %X', time.localtime())
            uid = str(uuid.uuid4()).replace('-', '')
            item = MysqldemoItem(mingyan=mingyan, zuoze=zuoze, ctime=ctime, uid=uid)
            yield item

        html_wraps = response.css('.page-navigator a:not(.next)::attr(href)').extract()
        for html_wrap in html_wraps:
            yield response.follow(url=html_wrap, callback=self.parse)