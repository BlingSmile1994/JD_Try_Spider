#! python3
# -*- coding: utf-8 -*-
# @Time    : 2017/9/1 上午1:06
# @Author  : BlingBling
# @File    : try_spider.py
# @Software: PyCharm Community Edition
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from jd.items import JdItem


class TrySpider(CrawlSpider):
    name = "tryspider"
    allowed_domains = ['try.jd.com']
    start_urls = ["https://try.jd.com/activity/getActivityList"]
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default). follow
        Rule(LinkExtractor(allow=('https://try.jd.com/activity/getActivityList'))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item. process
        Rule(LinkExtractor(allow=(r'https://try.jd.com/d+.html')), callback='parse_item'),
    )


    def parse_item(self, response):
        # current_url = response.url
        # body = response.body
        # unicode_body = response.body_as_unicode()
        # print(unicode_body)
        #hxs = HtmlXPathSelector(response)  # 创建查询对象
        sel = Selector(response)
        item = JdItem()
        item['name'] = sel.xpath('//*[@id="product-intro"]/div[2]/div[1]/span').extract()
        item['price'] = sel.xpath('//*[@id="product-intro"]/div[2]/div[3]/em/b').extract()
        item['endTime'] = sel.xpath('//*[@id="product-intro"]/@end_time').extract()
        item['startTime'] = sel.xpath('//*[@id="product-intro"]/@start_time').extract()
        item['applyNum'] = sel.xpath('//*[@id="product-intro"]/div[2]/div[4]/div[1]/div/div[1]/div/b[2]').extract()
        item['supplyNum'] = sel.xpath('//*[@id="product-intro"]/div[2]/div[4]/div[1]/div/div[1]/div/b[1]').extract()
        return item