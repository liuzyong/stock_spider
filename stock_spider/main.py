from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "stock"])
# execute(["scrapy", "crawl", "stock", "-o", "items.json"])
#
# # http://pycs.greedyai.com/

# from scrapy.cmdline import execute
# execute(["scrapy","crawl","stock","-o","items1.json"])