# -*- coding: utf-8 -*-
from urllib import parse

import scrapy

from stock_spider.items import StockItem


class StockSpider(scrapy.Spider):
    name = 'stock'
    # allowed_domains = ['pycs.greedyai.com']
    # start_urls = ['http://pycs.greedyai.com/']
    allowed_domains = ['quote.eastmoney.com']
    start_urls = ['http://quote.eastmoney.com']

    def parse(self, response):
        # 获取链接地址
        # post_urls = response.xpath("//a/@href").extract()
        # print(post_urls)

        # for post_url in post_urls:
        #     yield scrapy.Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detal, dont_filter= True )
        post_url = "zs000002.html"
        yield scrapy.Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detal, dont_filter=True)



    def parse_detal(self, response):
        # print("回调函数被调用")
        stock_item = StockItem()
        # 获取股票名称
        stock_item["names"]= self.get_names(response)
        # 获取股票代码
        stock_item["code"] = self.get_code(response)
        # 获取股票今开
        stock_item["today_open"] = self.get_today_open(response)
        # 获取股票昨收
        # stock_item["yes_close"]= self.get_yes_close(response)

        # 按照需求添加爬取得数据

        yield stock_item


    def get_names(self, response):
        # names = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()").extract()
        names = response.xpath("///*[@id=\"name\"]/text()").extract()
        print(names)
        return names

    # 获取股票代码
    def get_code(self, response):
        # //*[@id="ml_001"]/table/tbody/tr[1]/td[2]
        # infors = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[2]/text()").extract()
        # print(infors)
        code = response.xpath("///*[@id=\"code\"]/text()").extract()
        print(code)
        return code

    def get_today_open(self, response):
        # //*[@id="gt1"]
        # 在调试，目前获取不到
        today_open = response.xpath("///*[@id=\"gt1\"]").extract()
        print(today_open)
        return today_open
