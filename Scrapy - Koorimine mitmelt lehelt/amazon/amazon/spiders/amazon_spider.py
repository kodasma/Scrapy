# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 1
    start_urls = [
        'https://www.amazon.com/s?rh=n%3A18145289011&page=1&qid=1586342266&ref=lp_18145289011_pg_2'
    ]

    def parse(self, response):
        items = AmazonItem()

        books = response.css('li.s-result-item')

        for book in books:
            product_name = book.css('.s-access-title::text').extract()
            product_author = book.css('.a-color-secondary .a-text-normal').css('::text').extract()
            product_imagelink = book.css('.cfMarker::attr(src)').extract()

            items['product_name'] = product_name
            items['product_author'] = product_author
            items['product_imagelink'] = product_imagelink

            yield items

        next_page = 'https://www.amazon.com/s?rh=n%3A18145289011&page=' + str(AmazonSpiderSpider.page_number) + '&qid=1586342266&ref=lp_18145289011_pg_2'
        AmazonSpiderSpider.page_number += 1
        yield response.follow(next_page, callback=self.parse2)

    def parse2(self, response):
        items = AmazonItem()

        books = response.css('div.s-latency-cf-section')

        for book in books:
            product_name = book.css('.a-color-base.a-text-normal').css('::text').extract()
            product_author = book.css('.a-color-secondary .a-size-base:nth-child(2)').css('::text').extract()
            product_imagelink = book.css('.s-image-fixed-height .s-image::attr(src)').extract()

            items['product_name'] = product_name
            items['product_author'] = product_author
            items['product_imagelink'] = product_imagelink

            yield items

        next_page = 'https://www.amazon.com/s?rh=n%3A18145289011&page=' + str(AmazonSpiderSpider.page_number) + '&qid=1586342266&ref=lp_18145289011_pg_2'
        if AmazonSpiderSpider.page_number < 11:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse2)