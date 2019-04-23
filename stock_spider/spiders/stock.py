# -*- coding: utf-8 -*-
from urllib import parse

import scrapy

from items import StockstarItem,StockstarItemLoader
# from stock_spider.items import StockItem


class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['quote.stockstar.com']  # 定义爬虫域
    start_urls = ['http://quote.stockstar.com/stock/ranklist_a_3_1_1.html']  # 定义爬虫连接

    def parse(self, response):  # 撰写爬虫逻辑
        page = int(response.url.split("_")[-1].split(".")[0])  # 抓取页码
        item_nodes = response.css('#datalist tr')
        for item_node in item_nodes:
            # 根据item文件所定义的字段内容，进行字段内容的抓取
            item_loader = StockstarItemLoader(item=StockstarItem(), selector=item_node)
            item_loader.add_css("code", "td:nth-child(1) a::text")
            item_loader.add_css("abbr", "td:nth-child(2) a::text")
            item_loader.add_css("last_trade", "td:nth-child(3) span::text")
            item_loader.add_css("chg_ratio", "td:nth-child(4) span::text")
            item_loader.add_css("chg_amt", "td:nth-child(5) span::text")
            item_loader.add_css("chg_ratio_5min", "td:nth-child(6) span::text")
            item_loader.add_css("volumn", "td:nth-child(7)::text")
            item_loader.add_css("turn_over", "td:nth-child(8)::text")
            stock_item = item_loader.load_item()
            yield stock_item
        if item_nodes:
            next_page = page + 1
            next_url = response.url.replace("{0}.html".format(page), "{0}.html".format(next_page))
            yield scrapy.Request(url=next_url, callback=self.parse)


    # allowed_domains = ['pycs.greedyai.com']
    # start_urls = ['http://pycs.greedyai.com/']
    #
    # allowed_domains = ['quote.eastmoney.com']
    # start_urls = ['http://quote.eastmoney.com']
    #
    # def parse(self, response):
    #     # 获取链接地址
    #     # post_urls = response.xpath("//a/@href").extract()
    #     # print(post_urls)
    #
    #     # for post_url in post_urls:
    #     #     yield scrapy.Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detal, dont_filter= True )
    #     post_url = "zs000002.html"
    #     yield scrapy.Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detal, dont_filter=True)
    #
    #
    #
    # def parse_detal(self, response):
    #     # print("回调函数被调用")
    #     stock_item = StockItem()
    #     # 获取股票名称
    #     stock_item["names"]= self.get_names(response)
    #     # 获取股票代码
    #     stock_item["code"] = self.get_code(response)
    #     # 获取股票今开
    #     stock_item["today_open"] = self.get_today_open(response)
    #     # 获取股票昨收
    #     # stock_item["yes_close"]= self.get_yes_close(response)
    #
    #     # 按照需求添加爬取得数据
    #
    #     yield stock_item
    #
    #
    # def get_names(self, response):
    #     # names = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()").extract()
    #     names = response.xpath("///*[@id=\"name\"]/text()").extract()
    #     print(names)
    #     return names
    #
    # # 获取股票代码
    # def get_code(self, response):
    #     # //*[@id="ml_001"]/table/tbody/tr[1]/td[2]
    #     # infors = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[2]/text()").extract()
    #     # print(infors)
    #     code = response.xpath("///*[@id=\"code\"]/text()").extract()
    #     print(code)
    #     return code
    #
    # def get_today_open(self, response):
    #     # //*[@id="gt1"]
    #     # 在调试，目前获取不到   //*[@id="price9"]
    #     today_open = response.xpath("///*[@id=\"gt1\"]").extract()
    #     # today_open = response.xpath("///*[@id=\"price9\"]").extract()
    #     print(today_open)
    #     return today_open
