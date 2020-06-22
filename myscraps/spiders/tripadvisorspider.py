#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.responsetypes import Response
from myscraps.items import ReviewItem
from scrapy import Request

class TripAdvisorReview(scrapy.Spider):
    name = "tripadvisor"
    # Cities: Recife, Porto Alegre, Salvador, Brasilia, Fortaleza, Curitiba, Belo Horizonte, Vitoria, Florianopolis, Natal, Goiania.
    start_urls = ["https://www.tripadvisor.com/Hotels-g295366-Antigua_Sacatepequez_Department-Hotels.html"]

    def parse(self, response):
        urls = []
        for href in response.css('div.meta_listing').xpath('@data-url').extract():
            url = response.urljoin(href)
            if url not in urls:
                urls.append(url)

                yield scrapy.Request(url, callback=self.parse_page)

        next_page = response.css("a.nav.next").xpath('@href').get()
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse)

    def parse_page(self, response: Response):

        sub_div = response.css('div.location-review-review-list-parts-SingleReview__mainCol--1hApa')

        for review in sub_div:
            item = ReviewItem()

            contents = review.css(
                'q.location-review-review-list-parts-ExpandableReview__reviewText--gOmRC span::text').get()
            content = contents.encode("utf-8")

            ratings = review.css('span.ui_bubble_rating').xpath('@*').get()
            rating = int(ratings.split(' ')[-1].replace('bubble_', ''))
            
            rev_title = review.css('div.location-review-review-list-parts-ReviewTitle__reviewTitle--2GO9Z').css('span::text').get()
            #rev_title = rev_title.css('span::text').get()
            

            item['rating'] = rating
            item['title'] = rev_title
            item['review'] = content
            yield item

        next_page = response.css("a.nav.next").xpath('@href').get()
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse_page)



