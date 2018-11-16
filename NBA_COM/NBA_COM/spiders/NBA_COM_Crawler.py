# -*- coding: utf-8 -*-
import scrapy


class NbaComCrawlerSpider(scrapy.Spider):
    name = 'NBA_COM_Crawler'
    allowed_domains = ['https://stats.nba.com/teams/traditional/?sort=W_PCT']
    start_urls = ['http://stats.nba.com/teams/traditional/?sort=W_PCT/']

    def parse(self, response):
        pass
