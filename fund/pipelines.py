# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class FundPipeline(object):
    def process_item(self, item, spider):
        return item

###易方达基金
class YFDPipeline(object):
    def __init__(self):
        # connection database
        self.connect = pymysql.connect(host='localhost', user='root', passwd='cmcc1234',
                                       db='stock')  # 后面三个依次是数据库连接名、数据库密码、数据库名称
        # get cursor
        self.cursor = self.connect.cursor()
        print("连接数据库成功")

    def process_item(self, item, spider):
        # sql语句
        try:
            ###易方达
            if spider.name == 'funddetailspider':
                insert_sql = """insert into ts_fund_daily(fund_id, fund_time, fund_stock_rank, fund_stock_code, fund_stock_name,fund_stock_number,fund_stock_value,fund_stock_ratio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
                # 执行插入数据到数据库操作
                self.cursor.execute(insert_sql, (item['fund_id'], item['fund_time'], item['fund_stock_rank'], item['fund_stock_code'],
                                                 item['fund_stock_name'], item['fund_stock_number'], item['fund_stock_value'], item['fund_stock_ratio']))
            elif spider.name == 'fundspider':
                insert_sql = """insert into ts_fund(fund_id, fund_time, fund_name, fund_net_value, fund_day_rise,fund_this_year_rise,fund_year_rise,fund_risk) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
                # 执行插入数据到数据库操作
                self.cursor.execute(insert_sql, (
                item['fund_id'], item['fund_time'], item['fund_name'], item['fund_net_value'],
                item['fund_day_rise'], item['fund_this_year_rise'], item['fund_year_rise'], item['fund_risk']))
            ###中欧
            elif spider.name == 'zofundspider':
                insert_sql = """insert into zo_ts_fund(fund_id, fund_time, fund_name, fund_net_value, fund_day_rise,fund_this_year_rise,fund_year_rise,fund_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
                # 执行插入数据到数据库操作
                self.cursor.execute(insert_sql, (
                    item['fund_id'], item['fund_time'], item['fund_name'], item['fund_net_value'],
                    item['fund_day_rise'], item['fund_this_year_rise'], item['fund_year_rise'], item['fund_type']))

            elif spider.name == 'zofunddetailspider':
                insert_sql = """insert into zo_ts_fund_daily(fund_id, fund_time, fund_stock_rank, fund_stock_code, fund_stock_name,fund_stock_ratio) VALUES (%s,%s,%s,%s,%s,%s)"""
                # 执行插入数据到数据库操作
                self.cursor.execute(insert_sql, (
                item['fund_id'], item['fund_time'], item['fund_stock_rank'], item['fund_stock_code'],
                item['fund_stock_name'], item['fund_stock_ratio']))
            ###汇添富
            elif spider.name == 'htffundspider':
                insert_sql = """insert into htf_ts_fund(fund_id, fund_time, fund_name) VALUES (%s,%s,%s)"""
                # 执行插入数据到数据库操作
                self.cursor.execute(insert_sql, (
                    item['fund_id'], item['fund_time'], item['fund_name']))

            elif spider.name == 'htffunddetailspider':
                insert_sql = """insert into htf_ts_fund_daily(fund_id, fund_time, fund_stock_rank, fund_stock_code, fund_stock_name,fund_stock_ratio,fund_stock_compare) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                # 执行插入数据到数据库操作
                self.cursor.execute(insert_sql, (
                item['fund_id'], item['fund_time'], item['fund_stock_rank'], item['fund_stock_code'],
                item['fund_stock_name'], item['fund_stock_ratio'], item['fund_stock_compare']))
            # 提交，不进行提交无法保存到数据库
            self.connect.commit()
        except:
            pass

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()