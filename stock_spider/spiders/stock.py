# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from stock_spider.items import StockItem

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['pycs.greedyai.com']
    start_urls = ['http://pycs.greedyai.com/']

    def parse(self, response):
        # 获取链接地址
        post_urls = response.xpath("//a/@href").extract()
        # print(post_urls)

        for post_url in post_urls:
            yield scrapy.Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detal, dont_filter= True )



    def parse_detal(self, response):
        # print("回调函数被调用")
        stock_item = StockItem()
        stock_item["names"]= self.get_names(response)
        # print(stock_item["names"])

        stock_item["infos"] = self.get_infors(response)
        # print(stock_item["infos"])
        yield stock_item

    def get_names(self, response):
        names = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()").extract()
        print(names)
        return names

    # 获取职务信息
    def get_infors(self, response):
        # //*[@id="ml_001"]/table/tbody/tr[1]/td[2]
        infors = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[2]/text()").extract()
        print(infors)
        return infors

# response.xpath("//*[@id=\"price9\"]/data-bind").extract()
