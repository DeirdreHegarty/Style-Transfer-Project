# from webscraper.items import WebscraperItem
# import datetime

# scrapy shell
# fetch("https://www.vangoghmuseum.nl/en/search/collection/")


import scrapy
 
class imagespider(scrapy.Spider):
	name = "pyimagesearch-spider"
	#list of allowed domains
	allowed_domains = ['www.vincent-van-gogh-gallery.org']
	#starting url
	start_urls = ['https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96', 
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=2", 
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=3",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=4",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=5",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=6",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=7",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=8",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=9",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=10",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=11",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=12",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=13",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=14",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=15",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=16",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=17",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=18",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=19",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=20",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=21",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=22",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=23",
	"https://www.vincent-van-gogh-gallery.org/the-complete-works.html?ps=96&pageno=24"]

	#location of csv file
	custom_settings = {
		'FEED_URI' : 'tmp/scraped-images.csv'
	}

	def parse(self, response):

		getimages = response.css("img::attr(src)").extract()
		string = "https://www.vincent-van-gogh-gallery.org"
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


