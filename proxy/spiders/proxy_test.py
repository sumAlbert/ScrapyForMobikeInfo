# -*- coding: utf-8 -*-
from time import sleep

import scrapy

class Proxy_text(scrapy.Spider):
    name = 'proxy_test'
    def start_requests(self):
        urls = [
            'http://www.4399.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url , callback = self.parse , meta = {'proxy': '121.232.194.78:9000'})

    def parse(self, response):
        print ('123\n')
        print response.css('h1#ipd>span::text').extract()
        pass