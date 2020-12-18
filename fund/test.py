"""
from scrapy import cmdline
cmdline.execute("scrapy crawl testspider5".split())
"""

import requests

url = 'http://icanhazip.com'
proxy = {'http':'180.119.94.184:9999'}


resp = requests.get(url,proxies=proxy).text

print(resp)