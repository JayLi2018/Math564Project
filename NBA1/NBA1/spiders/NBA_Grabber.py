# -*- coding: utf-8 -*-
import scrapy


class NbaGrabberSpider(scrapy.Spider):
	name = 'NBA_Grabber'
	# allowed_domains = ['insider.espn.com/nba/hollinger/statistics/_/year/2017']
	start_urls = ['http://insider.espn.com/nba/hollinger/statistics/_/year/2018/'
	               ]

	def parse(self, response):
		players = response.xpath('.//tr[starts-with(@class, "oddrow")]|.//tr[starts-with(@class, "evenrow")]')

		for player in players:

			rk = player.xpath('.//td[1]/text()').extract_first()
			player_name = player.xpath('.//td[2]/a/text()').extract_first()
			teams = player.xpath('.//td[2]/text()').extract()[0].split(", ")[1]  
			gp = player.xpath('.//td[3]/text()').extract_first() 
			mpg = player.xpath('.//td[4]/text()').extract_first()
			ts = player.xpath('.//td[5]/text()').extract_first()
			ast = player.xpath('.//td[6]/text()').extract_first()
			to = player.xpath('.//td[7]/text()').extract_first()
			usg = player.xpath('.//td[8]/text()').extract_first()
			orr = player.xpath('.//td[9]/text()').extract_first()
			drr = player.xpath('.//td[10]/text()').extract_first()
			rebr = player.xpath('.//td[11]/text()').extract_first()
			per = player.xpath('.//td[@class="sortcell"]/text()').extract_first()
			va = player.xpath('.//td[13]/text()').extract_first()
			ewa = player.xpath('.//td[14]/text()').extract_first()
			
			teams_list = teams.split("/")  # there are some players get traded 
			for team in teams_list:
				yield{'RK':rk,
				'PLAYER':player_name,
				'TEAM':team,
				'GP':gp,
				'MPG':mpg,
				'TS':ts,
				'AST':ast,
				'TO':to,
				'USG':usg,
				'ORR':orr,
				'DRR':drr,
				'REBR':rebr,
				'PER':per,
				'VA':va,
				'EWA':ewa
				}

		next_page_url_list = response.xpath('//div[@class="controls"]/a[@rel = "nofollow"]/@href').extract()
		if(len(next_page_url_list) ==1):
			next_page_url = next_page_url_list[0]
			print("found next page!")
		else:
			next_page_url = next_page_url_list[1]
			print("found next page!")
		absolute_next_url = 'http://'+next_page_url
		yield scrapy.Request(absolute_next_url)
