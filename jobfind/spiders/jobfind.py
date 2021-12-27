import scrapy


class JobFindSpider(scrapy.Spider):
    name = 'jobfind'
    # allowed_domains = ['example.com']
    start_urls = ['https://www.indeed.com/jobs?q=software%20engineer%20intern&fromage=7']

    # def start_requests(self):
    #     return [scrapy.Request(url=url, callback=self.parse) for url in self.start_urls]

    def parse(self, response, **kwargs):
        print(response.url)

        # May need to refactor when working on job finding for LinkedIn
        job_cards_containers = response.css('div#mosaic-provider-jobcards')
        if len(job_cards_containers) != 1:
            print('Could not find job cards container')
            return

        job_cards_links = job_cards_containers[0].css('a.resultWithShelf::atr(href)').extract()
        job_cards = job_cards_containers[0].css('a.resultWithShelf')

        for job_card in job_cards:
            job_title = job_card.css('h2.')

        # yield response.url
