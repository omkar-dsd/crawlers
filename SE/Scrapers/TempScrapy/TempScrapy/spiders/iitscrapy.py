from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from TempScrapy.items import TempscrapyItem

class IitscrapySpider(CrawlSpider):
    name = 'iitscrapy'
    allowed_domains = ['cse.iitd.ernet.in/~naveen/']
    start_urls = ['http://www.cse.iitd.ernet.in/~naveen/']

    # rules = (
    #     Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = TempscrapyItem()

        i['Content'] = hxs.select('/html/body/table/tbody/tr[3]/td[1]/text()[1]').extract()
        i['Source_Website'] = "http://www.cse.iitd.ernet.in/~naveen/"
        print i
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        return i
