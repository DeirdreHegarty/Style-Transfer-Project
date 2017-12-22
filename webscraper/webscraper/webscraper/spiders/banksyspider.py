import scrapy
 
class imagespider(scrapy.Spider):
	name = "banksy-spider"
	#list of allowed domains
	allowed_domains = ['www.artnet.com/artists/banksy']
	#starting url
	start_urls = ["http://www.artnet.com/artists/banksy/" + str(x) for x in range(116)]

	#location of csv file
	custom_settings = {
		'FEED_URI' : 'tmp/banksy-images.csv'
	}

	def parse(self, response):

		image = response.css(".details-link img::attr(src)").extract()

		title = response.css(".details-link img::attr(title)").extract()


		for item in zip(image, title):
			scraped_info = {
				'image_urls': [item[0]],
				'title'	: [item[1]]
				
			}
			yield scraped_info