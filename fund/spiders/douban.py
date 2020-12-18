import scrapy
import json
from fund.items import DoubanMovieItem

class MySpider1(scrapy.Spider):
    # 设置name
    name = "doubanmovie"
    # 填写爬取地址
    start_urls = []

    for i in range(0,1000,20):
        url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start='+str(i)
        start_urls.append(url)

    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))
        cnt=0
        for info in infos['data']:
            movie_url_detail = info['url']
            print(movie_url_detail)
            yield scrapy.Request(movie_url_detail,callback=self.parse_movie)

    def parse_movie(self, response):
        line = response.xpath('//div[@id="info"]')
        item = DoubanMovieItem()
        #导演
        director = line.xpath('./span[1]/span[2]')
        item['director'] = director.xpath('string(.)').extract_first()
        #编剧
        writer = line.xpath('./span[2]/span[2]')
        item['writer'] = writer.xpath('string(.)').extract()
        #演员
        actor = line.xpath('.//span[@class="actor"]/span[@class="attrs"]')
        item['actor'] = actor.xpath('string(.)').extract()
        #分类
        item['classify'] = '/'.join(line.xpath('.//span[@property="v:genre"]/text()').extract())
        #上映日期
        item['open_dt'] = line.xpath('.//span[@property="v:initialReleaseDate"]/text()').extract()
        #电影时长
        item['movie_length'] = line.xpath('.//span[@property="v:runtime"]/text()').extract()
        #评级
        item['rate'] = response.xpath('//strong[@property="v:average"]/text()').extract()
        #评分人数
        item['rate_num'] = response.xpath('//span[@property="v:votes"]/text()').extract()
        #电影简介
        movie_summary = response.xpath('.//span[@property="v:summary"]')
        item['movie_summary'] = movie_summary.xpath('string(.)').extract_first()
        #电影名称
        item['movie_name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()
        #年份
        item['movie_year'] = response.xpath('//span[@class="year"]/text()').extract()

        yield item
