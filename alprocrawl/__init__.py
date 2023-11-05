import scrapy

class GamePricesSpider(scrapy.Spider):
    name = 'game_prices'
    start_urls = ['https://bit.ly/scrapingtry']

    def parse(self, response):
        games = response.css('.game')
        for game in games:
            title = game.css('.title::text').get()
            price = game.css('.price::text').get()
            yield {
                'Title': title,
                'Price': price,
            }
