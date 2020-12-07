import scrapy
from fund.items import FundItem
from fund.items import FundDetailItem

###获取易方达基金情况
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
        cnt = 0
        for line in response.xpath('//*[@id="allFundTable"]/tbody/tr[@data-type="01" or @data-type="02"]'):
            # 初始化item对象保存爬取的信息
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['fund_name'] = line.xpath(
                './@data-name').extract()
            item['fund_id'] = line.xpath(
                './@data-code').extract()
            item['fund_time'] = line.xpath(
                './td[3]/text()').extract()
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

import re
###获取易方达基金投资组合
class MySpider2(scrapy.Spider):
    # 设置name
    name = "funddetailspider"
    start_urls = []
    test=['110001','110002','110005','110009','110010','110011','110012','110013','110015','110022','110023','110025','110029','112002','161131','161132','506002','001018','001076','001136','001182','001184','001216','001217','001249','001285','001286','001314','001315','001342','001343','001373','001382','001433','001437','001438','001441','001442','001443','001444','001475','001513','001562','001603','001745','001746','001747','001748','001802','001803','001806','001807','001817','001818','001832','001835','001836','001856','001857','001898','002216','002217','002602','002910','003293','003839','003840','003882','003883','003961','003962','005438','005583','005827','005875','005876','005877','005955','005956','006013','006014','006533','007346','007548','007884','008283','008286','009049','009215','009216','009247','009248','009249','009250','009265','009341','009342','009412','009413','009689','009690','009808','009810','009811','009812','009813','009900','009901','009902','009903','010013','010317','010340','010387','010388','010389','010390','010650','000404','000436','000603']
    for t in test:
        for year in range(2010,2021):
            for type in [0,1,3,4]:
                fund_url = "http://query2.efunds.com.cn/website/assetinfo_detail.jsp?fundcode="+str(t)+"&reportYear="+str(year)+"&reportType="+str(type)
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