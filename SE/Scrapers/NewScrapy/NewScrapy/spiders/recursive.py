from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from NewScrapy.items import NewscrapyItem
import re

class RecursiveSpider(CrawlSpider):
    name = 'recursive'
    allowed_domains = ['cse.iitd.ernet.in']
    start_urls = ['http://www.cse.iitd.ernet.in/~naveen/']

    rules = (
        Rule(SgmlLinkExtractor(allow=('cse\.iitd\.ernet\.in/\~naveen/.*', )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = NewscrapyItem()
        i['URL'] = response.request.url 
        i['content'] = hxs.select('/html/body/table/tbody/tr[3]/td[1]/text()[1]').extract()
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        return i
