import scrapy
import json
from fund.items import DoubanMovieItem

class MySpider1(scrapy.Spider):
    # 设置name
    name = "doubanmovie"
    # 填写爬取地址

    start_urls = ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0']

    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))
        cnt=0
        for info in infos['data']:
            cnt+=1
            if cnt==2:
                break
            movie_url_detail = info['url']
            yield scrapy.Request(movie_url_detail,callback=self.parse_movie)

    def parse_movie(self, response):
        line = response.xpath('//div[@id="info"]')
        item = DoubanMovieItem()
        item['director'] = line.xpath('./span[1]/span[2]/a/text()').extract_first()
        writer = line.xpath('./span[2]/span[2]/a')
        item['writer'] = writer.xpath('string(.)').extract()
        actor = line.xpath('.//span[@class="attrs"]/span')
        item['actor'] = actor.xpath('string(.)').extract()

        yield item
