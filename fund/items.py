# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class FundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fund_name = scrapy.Field()
    fund_id = scrapy.Field()
    fund_time = scrapy.Field()
    fund_net_value = scrapy.Field()
    fund_day_rise = scrapy.Field()
    fund_this_year_rise = scrapy.Field()
    fund_year_rise = scrapy.Field()
    fund_risk = scrapy.Field()

class FundDetailItem(scrapy.Item):
    fund_id = scrapy.Field()
    fund_time = scrapy.Field()
    fund_stock_rank = scrapy.Field()
    fund_stock_code = scrapy.Field()
    fund_stock_name = scrapy.Field()
    fund_stock_number = scrapy.Field()
    fund_stock_value = scrapy.Field()
    fund_stock_ratio = scrapy.Field()
