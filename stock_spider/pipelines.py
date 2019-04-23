# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class StockSpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class StockPipeline(object):
    def process_item(self, item, spider):
        # 数据持久化
        self.save_to_file(item)
        # print(item)
        return item

    def save_to_file(self, item):
        try:
            filename = "quote.cvs"
            file = open(filename, mode='a+')
            # 判断文件是否非空
            if 0 == os.path.getsize(filename):
                file.write("股票代码,股票简称,最新价,涨跌幅,涨跌额,5分钟涨幅,成交量,成交额\n")

            file.write(str(item["code"] + ","+ item["abbr"] + ","+ item["last_trade"] +","+ item["chg_ratio"] +","+  item["chg_amt"] +","+ item["chg_ratio_5min"] +","+ item["volumn"] +","+ item["turn_over"])+"\n")
            file.flush()
            file.close()
        except():
            pass

