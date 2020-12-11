import scrapy
from fund.items import TESTItem
from fund.items import TESTAUTHORItem
from scrapy.linkextractors import LinkExtractor


###爬取主页信息
class MySpider1(scrapy.Spider):
    # 设置name
    name = "testspider1"
    # 填写爬取地址

    start_urls = ['http://quotes.toscrape.com/']

    # 编写爬取方法
    def parse(self, response):
        item = TESTItem()

        for line in response.xpath('//div[@class="row"]/div[@class="col-md-8"]/div[@class="quote"]'):
            # 初始化item对象保存爬取的信息
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['author'] = line.xpath(
                './span[2]/small/text()').extract()
            item['text'] = line.xpath(
                './span[1]/text()').extract()

            yield item

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


###多层爬取，爬取作者信息
class MySpider2(scrapy.Spider):
    # 设置name
    name = "testspider2"
    # 填写爬取地址

    start_urls = ['http://quotes.toscrape.com/']

    # 编写爬取方法
    def parse(self, response):

        for line in response.xpath('//div[@class="row"]/div[@class="col-md-8"]/div[@class="quote"]'):
            test_url = line.xpath(
                './span[2]/a/@href').extract()[0]
            test_url = response.urljoin(test_url)
            test_url+='/'
            yield scrapy.Request(test_url, callback=self.parse_author)

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


    def parse_author(self,response):
        item = TESTAUTHORItem()
        item['name'] = response.xpath('/html/body/div/div[2]/h3/text()').extract()
        item['birthday'] = response.xpath('//span[@class="author-born-date"]/text()').extract()
        item['bio'] = response.xpath('//div[@class="author-description"]/text()').extract()
        yield item


###爬取源码
class MySpider3(scrapy.Spider):
    # 设置name
    name = "testspider3"
    # 填写爬取地址

    start_urls = ['https://matplotlib.org/examples/']

    # 编写爬取方法
    def parse(self, response):

        le = LinkExtractor(restrict_xpaths='//div[contains(@class,"toctree-wrapper")]//li[@class="toctree-l2"]/a')
        links = le.extract_links(response)
        cnt=0
        for link in links:
            print(link.url)
            cnt+=1
        print(cnt)