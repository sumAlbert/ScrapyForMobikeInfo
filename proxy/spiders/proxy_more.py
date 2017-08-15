# -*- coding: utf-8 -*-
from time import sleep

import scrapy

class Proxy_more(scrapy.Spider):
    name = 'proxy_more'
    def start_requests(self):
        url_fix = 'http://www.kuaidaili.com/free/inha/'
        urls = []
        for num in xrange(1,20):
            urls.append(url_fix+str(num)+'/')
        for url in urls:
            yield scrapy.Request(url=url , callback = self.parse, meta={'proxy':'http://223.240.208.87:3128'})

    def parse(self, response):
        ips =  response.css('td[data-title=IP]::text').extract()
        ports = response.css('td[data-title=PORT]::text').extract()
        for num in xrange(0,15):
            print ips[num]+':'+ports[num]
            with open('./second_proxy.txt','a') as fp:
                fp.write(ips[num]+':'+ports[num]+'\n')
