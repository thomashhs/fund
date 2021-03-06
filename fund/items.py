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

###中欧基金概况
class ZOFundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fund_name = scrapy.Field()
    fund_id = scrapy.Field()
    fund_type = scrapy.Field()
    fund_time = scrapy.Field()
    fund_net_value = scrapy.Field()
    fund_day_rise = scrapy.Field()
    fund_this_year_rise = scrapy.Field()
    fund_year_rise = scrapy.Field()

###中欧基金组合
class ZOFundDetailItem(scrapy.Item):
    fund_id = scrapy.Field()
    fund_time = scrapy.Field()
    fund_stock_rank = scrapy.Field()
    fund_stock_code = scrapy.Field()
    fund_stock_name = scrapy.Field()
    fund_stock_ratio = scrapy.Field()


###汇添富基金概况
class HTFFundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fund_name = scrapy.Field()
    fund_id = scrapy.Field()
    fund_time = scrapy.Field()

###汇添富基金组合
class HTFFundDetailItem(scrapy.Item):
    fund_id = scrapy.Field()
    fund_time = scrapy.Field()
    fund_stock_rank = scrapy.Field()
    fund_stock_code = scrapy.Field()
    fund_stock_name = scrapy.Field()
    fund_stock_ratio = scrapy.Field()
    fund_stock_compare = scrapy.Field()

###交银施罗德基金概况
class JYSLDFundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fund_name = scrapy.Field()
    fund_id = scrapy.Field()
    fund_time = scrapy.Field()
    fund_type = scrapy.Field()

###交银施罗德基金组合
class JYSLDFundDetailItem(scrapy.Item):
    fund_id = scrapy.Field()
    fund_time = scrapy.Field()
    fund_stock_name = scrapy.Field()
    fund_stock_ratio = scrapy.Field()

###天天基金概况
class TTFundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fund_name = scrapy.Field()
    fund_id = scrapy.Field()

###天天基金组合
class TTFundDetailItem(scrapy.Item):
    fund_id = scrapy.Field()
    fund_time = scrapy.Field()
    fund_stock_name = scrapy.Field()
    fund_stock_ratio = scrapy.Field()

###测试用
class TESTItem(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()

###测试用
class TESTAUTHORItem(scrapy.Item):
    name = scrapy.Field()
    birthday = scrapy.Field()
    bio = scrapy.Field()

###测试用
class TESTFILEItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()

###测试用
class TESTIMAGEItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()

###测试用
class TESTLOGINItem(scrapy.Item):
    info = scrapy.Field()



###豆瓣电影
class DoubanMovieItem(scrapy.Item):
    director = scrapy.Field()
    writer = scrapy.Field()
    actor = scrapy.Field()
    classify = scrapy.Field()
    open_dt = scrapy.Field()
    movie_length = scrapy.Field()
    rate = scrapy.Field()
    rate_num = scrapy.Field()
    movie_summary = scrapy.Field()
    movie_name = scrapy.Field()
    movie_year = scrapy.Field()


###豆瓣音乐
class DoubanMusicItem(scrapy.Item):
    music_name = scrapy.Field()
    music_info = scrapy.Field()
