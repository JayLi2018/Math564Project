# -*- coding: utf-8 -*-
import scrapy


class RankCollectoSpider(scrapy.Spider):
	name = 'rank_collecto'
	allowed_domains = ['www.espn.com/nba/standings/_/season/2018/group/league']
	start_urls = ['http://www.espn.com/nba/standings/_/season/2018/group/league/']

	def parse(self, response):
		team_names = response.xpath('//td[@class = "v-top"]/table/tbody/tr')
		teams_stats = response.xpath('//td[@class = "v-top"]/div/div/div/table/tbody/tr/td/table/tbody/tr')

		for n in range(0,30):
			team_name = team_names[n].xpath('.//span[@class = "dn show-mobile"]/a/abbr/text()').extract()
			team_stat = teams_stats[n]
			win = team_stat.xpath('.//td[1]/span/text()').extract()
			loss = team_stat.xpath('.//td[2]/span/text()').extract()
			pct = team_stat.xpath('.//td[3]/span/text()').extract()
			home = team_stat.xpath('.//td[5]/span/text()').extract()
			away  = team_stat.xpath('.//td[6]/span/text()').extract()
			div = team_stat.xpath('.//td[7]/span/text()').extract()
			conf = team_stat.xpath('.//td[8]/span/text()').extract()
			ppg = team_stat.xpath('.//td[9]/span/text()').extract()
			opp_ppg = team_stat.xpath('.//td[10]/span/text()').extract()
			diff = team_stat.xpath('.//td[11]/span/text()').extract()
			
			print(team_name)
			print(diff)
				
			yield{'team_name': team_name,
			 'win':win,
			 'loss':loss,
			 'pct':pct,
			 'home':home,
			 'away':away,
			 'div':div,
			 'conf': conf, 
			 'ppg': ppg,
			 'opp_ppg':opp_ppg,
			 'diff':diff
			}