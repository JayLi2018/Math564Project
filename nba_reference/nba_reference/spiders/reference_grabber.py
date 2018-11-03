# -*- coding: utf-8 -*-
import scrapy


class ReferenceGrabberSpider(scrapy.Spider):
	name = 'reference_grabber'
	# allowed_domains = ['www.basketball-reference.com/leagues/NBA_2018_per_game.html']
	start_urls = ['http://www.basketball-reference.com/leagues/NBA_2014_per_game.html/']

	def parse(self, response):
		players_stats = response.xpath('//div[@id="all_per_game_stats"]/div[starts-with(@class,"table")]/div[starts-with(@class,"overthrow")]/table/tbody/tr[starts-with(@class,"full_table")]|//div[@id="all_per_game_stats"]/div[starts-with(@class,"table")]/div[starts-with(@class,"overthrow")]/table/tbody/tr[starts-with(@class,"italic")]')
		
		for player in players_stats:
			player_name =  player.xpath('.//td[1]/a/text()').extract() 
			position = player.xpath('.//td[2]/text()').extract()  
			age = player.xpath('.//td[3]/text()').extract()  
			team = player.xpath('.//td[4]/a/text()').extract()  
			gp = player.xpath('.//td[5]/text()').extract()  
			gs = player.xpath('.//td[6]/text()').extract()  
			mpg = player.xpath('.//td[7]/text()').extract()  
			FG = player.xpath('.//td[8]/text()').extract()  
			FGa = player.xpath('.//td[9]/text()').extract()  
			FGp = player.xpath('.//td[10]/text()').extract()  
			Three_PPG = player.xpath('.//td[11]/text()').extract()  
			Three_PA = player.xpath('.//td[12]/text()').extract()  
			Three_PP = player.xpath('.//td[13]/text()').extract()  	
			Two_PPG= player.xpath('.//td[14]/text()').extract()  
			Two_PA = player.xpath('.//td[15]/text()').extract()  
			Two_PP = player.xpath('.//td[16]/text()').extract()  
			eFGp = player.xpath('.//td[17]/text()').extract()  
			FT = player.xpath('.//td[18]/text()').extract()  
			FTa = player.xpath('.//td[19]/text()').extract()  
			FTp = player.xpath('.//td[20]/text()').extract()  
			orb = player.xpath('.//td[21]/text()').extract()  
			drb = player.xpath('.//td[22]/text()').extract()  
			trb = player.xpath('.//td[23]/text()').extract()  
			ast = player.xpath('.//td[24]/text()').extract()  
			stl = player.xpath('.//td[25]/text()').extract()  
			blk = player.xpath('.//td[26]/text()').extract()  
			tov = player.xpath('.//td[27]/text()').extract()  
			PF = player.xpath('.//td[28]/text()').extract()  
			ppg = player.xpath('.//td[29]/text()').extract() 

			yield{'player_name':player_name,
			'position':position,
			'age':age,
			'team':team,
			'gp':gp,
			'gs':gs,
			'mpg':mpg,
			'FG':FG,
			'FGa':FGa,
			'FGp':FGp,
			'3_PPG':Three_PPG,
			'3_PA':Three_PA,
			'3_PP':Three_PP,
			'2_PPG':Two_PPG,
			'2_PA':Two_PA,
			'2_PP':Two_PP,
			'FT':FT,
			'FTa':FTa,
			'FTp':FTp,
			'orb':orb,
			'drb':drb,
			'trb':trb,
			'ast':ast,
			'stl':stl,
			'blk':blk,
			'tov':tov,
			'PF':PF,
			'ppg':ppg
			} 








