import scrapy
import re
from ast import literal_eval
from fund.items import TTFundItem
from fund.items import TTFundDetailItem

###获取天天基金总体情况
class MySpider1(scrapy.Spider):
    # 设置name
    name = "ttfundspider"
    # 填写爬取地址

    start_urls = []
    # 股票型一共有8页
    for i in range(1,9):
        start_urls.append("http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=2&letter=&gsid=&text=&sort=zdf,desc&page="+str(i)+",200&dt=1607515044664&atfc=&onlySale=0")
    # 混合型一共有8页
    for i in range(1,24):
        start_urls.append(
            "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=3&letter=&gsid=&text=&sort=zdf,desc&page=" + str(
                i) + ",200&dt=1607520324122&atfc=&onlySale=0")
    # 编写爬取方法
    def parse(self, response):
        item = TTFundItem()
        test = response.text
        test = re.findall('datas:\[(.*?)\],count', test)[0]
        test = literal_eval(test)

        for t in test:
            item['fund_id'] = t[0]
            item['fund_name'] = t[1]

            yield item


###获取天天基金投资组合
class MySpider2(scrapy.Spider):
    # 设置name
    name = "ttfunddetailspider"
    fund_ids = []

    with open(r'C:\Users\34587\fund\tt_fund_id.txt') as f:
        for line in f.readlines():
            fund_ids.append(line.strip())
    start_urls = []
    for fund_id in fund_ids:
        fund_url = "http://fund.eastmoney.com/"+fund_id+".html"
        start_urls.append(fund_url)
    # 编写爬取方法
    with open(r'C:\Users\34587\fund\log.txt','w') as f:
        f.write(str(start_urls))

    def parse(self, response):
        item = TTFundDetailItem()
        url = response.url
        fund_id = url.split('/')[-1][:6]
        cnt=0
        for line in response.xpath('(//li[@class="position_shares"])[1]/div[1]/table/tr[position()>1]'):
            # 初始化item对象保存爬取的信息
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['fund_id'] = fund_id
            item['fund_time'] = '20200930'
            item['fund_stock_name'] = line.xpath(
                './td[1]/a/text()').extract()[0].strip()
            item['fund_stock_ratio'] = line.xpath(
                './td[2]/text()').extract()[0].strip()

            yield item