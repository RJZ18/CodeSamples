import scrapy


class QuotesSpider(scrapy.Spider):
    name = "nasdaq"
    start_urls = [
        'https://www.nasdaq.com/symbol/aapl/dividend-history'
    ]

    def parse(self, response):
        for quote in response.css('table[id=quotes_content_left_dividendhistoryGrid] tbody tr'):
            yield {
		        'response':response,
                'exDate': quote.css('span::text')[0].extract(), #You can either used regex or map it to a list position
                'cashAmount': quote.css('span::text')[1].extract(),
		        'declarationDate': quote.css('span::text')[2].extract(),
		        'recordDate': quote.css('span::text')[3].extract(),
		        'payDate': quote.css('span::text')[4].extract()
            }

	    newLink = '/symbol/msft/dividend-history'
	    nextLink = response.urljoin(newLink)
	    yield scrapy.Request(nextLink, callback=self.parse)

