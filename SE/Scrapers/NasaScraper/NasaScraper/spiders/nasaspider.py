from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from NasaScraper.items import NasascraperItem
import re

class NasaspiderSpider(CrawlSpider):
    name = 'nasaspider'
    allowed_domains = ['nasa.gov']
    start_urls = ['http://science.nasa.gov/missions/']

    rules = (
        Rule(SgmlLinkExtractor(allow=('science\.nasa\.gov/missions/.*', )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = NasascraperItem()

        i['URL'] = response.request.url 
        i['Phase'] = hxs.select('//*[@id="content"]/div[1]/div[1]/p[3]/text()').extract()
        i['Launch_Date'] = hxs.select(('//*[@id="content"]/div[1]/div[1]/p[4]/text()')).extract()
        i['Content'] = hxs.select('//*[@id="content"]/div[1]/div[1]/p[2]/text()').extract() 

        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        return i
