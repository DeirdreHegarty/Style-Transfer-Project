
import scrapy
 
class imagespider(scrapy.Spider):
	name = "dali-spider"
	#list of allowed domains
	allowed_domains = ['www.art.com/gallery/id--a126/salvador-dali-posters.htm']
	#starting url
	start_urls = ['https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=1&pathNumber=0',
	'https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=1&pathNumber=1',
	'https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=2&pathNumber=1',
	'https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=3&pathNumber=1',
	'https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=4&pathNumber=1',
	'https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=5&pathNumber=1',
	'https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=6&pathNumber=1',
	'https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=7&pathNumber=1',
	'https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=8&pathNumber=1',
	'https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=9&pathNumber=1',
	'https://www.art.com/gallery/id--a126/salvador-dali-posters.htm?Page=10&pathNumber=1'
	]

	#location of csv file
	custom_settings = {
		'FEED_URI' : 'tmp/dali-images.csv'
	}

	def parse(self, response):

		timages = response.css(".product-container img::attr(src)").extract()
		image = [str(x).strip()[0:x.index('?',0,-5)] for x in timages]

		title = response.css(".product-title::text").extract()


		for item in zip(image, title):
			scraped_info = {
				'image_urls': [item[0]],
				'title'	: [item[1]]
				
			}
			yield scraped_info