# from webscraper.items import WebscraperItem
# import datetime

# scrapy shell
# fetch("https://www.vangoghmuseum.nl/en/search/collection/")


import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
 
class imagespider(scrapy.Spider):
	name = "pyimagesearch-spider"
	#list of allowed domains
	allowed_domains = ['www.vangoghmuseum.nl/en/search/collection']
	#starting url
	start_urls = ['https://www.vangoghmuseum.nl/en/search/collection?q=&pagesize=10']
	#location of csv file
	custom_settings = {
		'FEED_URI' : 'tmp/scraped-images.csv'
	}

	def parse(self, response):

		getimages = response.css(".link-teaser::attr(href)").extract()
		string = "https://www.vangoghmuseum.nl"
		images = [string + x for x in getimages]



		# title = response.css(".text-base::text").extract()
		# new_title = [str(x).strip()[:x.index(',')].strip('\n') for x in title]


		artist = response.css(".col p::text").extract()



		for item in zip(images, images, artist):
			scraped_info = {
				'images': [item[0]],
				'image_urls': [item[1]],
				'artist': [item[2]] #Set's the url for scrapy to download images
				# 'title'	: [item[1]],
				
			}
			yield scraped_info


