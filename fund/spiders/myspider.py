import scrapy
from fund.items import FundItem
from fund.items import FundDetailItem
import re

###获取易方达基金总体情况
class MySpider1(scrapy.Spider):
    # 设置name
    name = "fundspider"
    # 填写爬取地址
    start_urls = [
        "http://www.efunds.com.cn/",
    ]

    # 编写爬取方法
    def parse(self, response):
        item = FundItem()
        #股票型或混合型基金
        for line in response.xpath('//*[@id="allFundTable"]/tbody/tr[@data-type="01" or @data-type="02"]'):
            # 初始化item对象保存爬取的信息
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['fund_name'] = line.xpath(
                './@data-name').extract()
            item['fund_id'] = line.xpath(
                './@data-code').extract()
            item['fund_time'] = ''.join(line.xpath(
                './td[3]/text()').extract()[0].split('-'))
            item['fund_net_value'] = line.xpath(
                './td[4]/span/text()').extract()
            item['fund_day_rise'] = line.xpath(
                './td[5]/span/text()').extract()
            item['fund_this_year_rise'] = line.xpath(
                './td[6]/span/text()').extract()
            item['fund_year_rise'] = line.xpath(
                './td[7]/span/text()').extract()
            item['fund_risk'] = line.xpath(
                './td[9]/text()').extract()

            yield item


###获取易方达基金投资组合
class MySpider2(scrapy.Spider):
    # 设置name
    name = "funddetailspider"
    fund_ids = []
    with open(r'C:\Users\34587\fund\fund_id.txt') as f:
        for line in f.readlines():
            fund_ids.append(line.strip())
    start_urls = []
    for fund_id in fund_ids:
        for year in range(2010,2021):
            for type in [0,1,3,4]:
                fund_url = "http://query2.efunds.com.cn/website/assetinfo_detail.jsp?fundcode="+str(fund_id)+"&reportYear="+str(year)+"&reportType="+str(type)
                start_urls.append(fund_url)
    # 编写爬取方法

    def parse(self, response):
        dict={'0':'0331','1':'0630','3':'0930','4':'1231'}
        item = FundDetailItem()
        cnt = 0
        url = re.findall('=\d+',response.url)
        fund_id = url[0][1:]
        fund_time = url[1][1:]+dict[url[2][1:]]
        for line in response.xpath('(//div[@class="asset-info"])[2]/table/tbody/tr'):
            # 初始化item对象保存爬取的信息
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['fund_id'] = fund_id
            item['fund_time'] = fund_time
            item['fund_stock_rank'] = line.xpath(
                './td[1]/text()').extract()
            item['fund_stock_code'] = line.xpath(
                './td[2]/text()').extract()
            item['fund_stock_name'] = line.xpath(
                './td[3]/text()').extract()
            item['fund_stock_number'] = line.xpath(
                './td[4]/text()').extract()
            item['fund_stock_value'] = line.xpath(
                './td[5]/text()').extract()
            item['fund_stock_ratio'] = line.xpath(
                './td[6]/text()').extract()[0].strip()

            yield item