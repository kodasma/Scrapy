# -*- coding: utf-8 -*-
import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.com/b/ref=audible_BHP?ie=UTF8&node=18145289011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=D74741YZA7BRQ9KYAF9Z&pf_rd_r=D74741YZA7BRQ9KYAF9Z&pf_rd_t=101&pf_rd_p=d7492e89-3625-45d0-83d7-ecb412133ef1&pf_rd_p=d7492e89-3625-45d0-83d7-ecb412133ef1&pf_rd_i=283155'
    ]

    def parse(self, response):
        pass
