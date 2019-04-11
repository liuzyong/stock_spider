# -*- coding: utf-8 -*-
import scrapy


class TonghuashunSpider(scrapy.Spider):
    name = 'tonghuashun'
    allowed_domains = ['stockpage.10jqka.com.cn']
    start_urls = ['http://basic.10jqka.com.cn/000002/company.html']

    def parse(self, response):
        # //*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        #result = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()")
        tc_names = response.xpath("//*[@class=\"tc name\"]/a/text()").extract()

        for tcname in tc_names:
            print(tcname)
        pass
