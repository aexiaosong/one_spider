# -*- coding: utf-8 -*-
import scrapy

from one.items import OneItem


class OneLogSpider(scrapy.Spider):
    name = 'one_log'
    allowed_domains = ['wufazhuce.com']
    start_urls = ['http://wufazhuce.com/one/' + str(i) for i in range(2677)]

    def parse(self, response):
        one_item = OneItem()
        one_item['vol'] = response.xpath('//*[@id="main-container"]/div/div/div/div[2]/div[1]/text()').extract_first().strip()
        day = response.xpath('//*[@id="main-container"]/div/div/div/div[3]/div[2]/p[1]/text()').extract_first()
        month = response.xpath('//*[@id="main-container"]/div/div/div/div[3]/div[2]/p[2]/text()').extract_first()
        one_item['date'] = day + month
        one_item['content'] = response.xpath('//*[@id="main-container"]/div/div/div/div[3]/div[1]/text()').extract_first().strip()
        one_item['pic_url'] = response.xpath('//*[@id="main-container"]/div/div/div/div[1]/img/@src').extract_first()
        one_item['current_url'] = response.url
        yield one_item
