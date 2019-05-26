# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from urllib import parse
from ..items import MaoyanItem

class MySpider(RedisSpider):
    name = 'my'
    allowed_domains = ['maoyan.com']
    # start_urls = ['https://maoyan.com/films?showType=3&sortId=3']
    redis_key = "maoyan"

    def parse(self, response):
        # 构建下一页url地址
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        next_url = parse.urljoin(response.url, next_url)
        # 分组
        dd_list = response.xpath("//div[@class='movies-list']/dl//dd")
        for dd in dd_list:
            item = MaoyanItem()
            item["film_name"] = dd.xpath("./div[2]/a/text()").extract_first()
            item["film_href"] = dd.xpath("./div[2]/a/@href").extract_first()
            item["film_href"] = parse.urljoin(response.url,item["film_href"])
            item["score"] = dd.xpath("./div[3]//i/text()").extract()

            yield scrapy.Request(url=item["film_href"],callback=self.parse_detail,meta={"item":item})

        yield scrapy.Request(next_url,callback=self.parse)


    def parse_detail(self,response):
        item = response.meta["item"]
        item["film_detail"] = response.xpath("//div[@class='movie-brief-container']/ul//text()").extract()
        item["actor_name"] = response.xpath("//div[@class='tab-celebrity tab-content']/div/div[2]/ul//li/div/a/text()").extract()
        item["film_introduction"] = response.xpath("//div[@class='tab-desc tab-content active']/div[1]/div[2]/span/text()").extract_first()
        yield item
