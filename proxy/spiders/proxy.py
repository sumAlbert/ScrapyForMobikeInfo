# -*- coding: utf-8 -*-
from time import sleep

import scrapy

class Proxy(scrapy.Spider):
    name = 'proxy'
    def start_requests(self):
        url_fix = 'http://www.kuaidaili.com/free/inha/'
        urls = []
        for num in xrange(12,13):
            urls.append(url_fix+str(num)+'/')
        for url in urls:
            yield scrapy.Request(url=url , callback = self.parse)

    def parse(self, response):
        ips =  response.css('td[data-title=IP]::text').extract()
        ports = response.css('td[data-title=PORT]::text').extract()
        for num in xrange(0,15):
            print ips[num]+':'+ports[num]
            with open('./first_proxy.txt','a') as fp:
                fp.write("'"+ips[num]+":"+ports[num]+"',\n")
