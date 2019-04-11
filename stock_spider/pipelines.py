# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


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
        pass
