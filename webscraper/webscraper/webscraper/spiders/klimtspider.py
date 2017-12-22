import scrapy
 
class imagespider(scrapy.Spider):
	name = "klimt-spider"
	#list of allowed domains
	allowed_domains = ['www.art.com/gallery/id--a126/salvador-dali-posters.htm']
	#starting url
	start_urls = ['https://www.klimtgallery.org/the-complete-works.html?ps=96&pageno=1',
	'https://www.klimtgallery.org/the-complete-works.html?ps=96&pageno=2',
	'https://www.klimtgallery.org/the-complete-works.html?ps=96&pageno=3',
	'https://www.klimtgallery.org/the-complete-works.html?ps=96&pageno=4'
	]
	#location of csv file
	custom_settings = {
		'FEED_URI' : 'tmp/klimt-images.csv'
	}

	def parse(self, response):

		getimages = response.css("img::attr(src)").extract()
		string = "https://www.klimtgallery.org"
		images = [string + x for x in getimages]

		# artist = "Vincent Van Gogh"
		title = response.css(".tile a::text").extract()

		for item in zip(images, title):
			scraped_info = {
				'image_urls': [item[0]],
				# 'artist': [item[1]],
				'title'	: [item[1]]
				
			}
			yield scraped_info