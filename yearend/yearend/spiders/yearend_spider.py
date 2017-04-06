import scrapy

class YearendSpider(scrapy.Spider):
    name = 'yearend'
    start_urls = ['https://en.wikipedia.org/wiki/Billboard_Year-End']

    def parse(self, response):
        'Billboard Year-End Hot 100'
        hrefs = response.css('a[href*=Billboard_Year-End_Hot_100]::attr(href)') \
            .extract()

        for href in hrefs:
            new_url = response.urljoin(href)
            yield scrapy.Request(new_url, callback=self.parseYear)



    def parseYear(self, response):
            cells = response.css('.wikitable tr td')
            for i in range(100):
                if cells[3 * i + 1].css('a::text'):
                    song = cells[3 * i + 1].css('a::text').extract()[0]
                else:
                    song = cells[3 * i + 1].css('td::text').extract()[0]

                if cells[3 * i + 2].css('a::text'):
                    artist = cells[3 * i + 2].css('a::text').extract()[0]
                else:
                    artist = cells[3 * i + 2].css('td::text').extract()[0]

                yield {
                    'song': song,
                    'artist': artist,
                    'year': int(response.url[len(response.url) - 4:])
                }


