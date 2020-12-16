import scrapy
from fund.items import TESTItem
from fund.items import TESTAUTHORItem
from fund.items import TESTFILEItem
from fund.items import TESTIMAGEItem
from fund.items import TESTLOGINItem
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


###爬取matplotlib示例源码
###学习如何下载文件
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
            cnt+=1
            yield scrapy.Request(link.url,callback=self.parse_example)

    def parse_example(self, response):
        url = response.xpath('//a[contains(@class,"external")]/@href').extract_first()
        url = response.urljoin(url)
        print(url)
        item = TESTFILEItem()
        item['file_urls'] = [url]
        yield item



###爬取示例源码
###学习如何下载图片
import json

class MySpider4(scrapy.Spider):
    # 设置name
    name = "testspider4"
    # 填写爬取地址
    BASE_URL = 'https://image.so.com/zjl?ch=art&sn=%s&listtype=new&temp=1'
    start_urls = [BASE_URL%0]
    start_index = 0

    # 编写爬取方法
    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))
        item = TESTIMAGEItem()
        item['image_urls'] = [info['qhimg_downurl'] for info in infos['list']]
        yield item

        self.start_index+=infos['count']
        if self.start_index and self.start_index < 1000:
            yield scrapy.Request(self.BASE_URL%self.start_index,callback=self.parse)


###学习登录Spider
from scrapy.http import FormRequest

class MySpider5(scrapy.Spider):
    # 设置name
    name = "testspider5"
    # 填写爬取地址
    start_urls = ['http://example.python-scraping.com/places/default/user/profile']

    def start_requests(self):
        yield scrapy.Request('http://example.python-scraping.com/places/default/user/login',callback=self.login)

    def login(self,response):
        fd = {'email': '123@qq.com', 'password': 'qwer1234'}
        yield FormRequest.from_response(response, formdata=fd,callback=self.parse_login)

    def parse_login(self,response):
        if 'Welcome thomas' in response.text:
            yield from super().start_requests()

    # 编写爬取方法
    def parse(self, response):
        item = TESTLOGINItem()
        for line in response.xpath('//td[@class="w2p_fw"]'):
            item['info'] = line.xpath('./text()').extract_first()
            yield item


