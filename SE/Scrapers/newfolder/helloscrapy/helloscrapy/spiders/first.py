from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
#from helloscrapy.items import HelloscrapyItem

class FirstSpider(CrawlSpider):
    name = 'first'
    allowed_domains = ['reddit.com']
    start_urls = ['http://www.reddit.com/r/pics/']

   
    rules = [
       Rule(SgmlLinkExtractor(allow=['.*']))
    ]
    # rules = (
    #     Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    # extract information from the website using parse

    # def parse_item(self, response):
    #     hxs = HtmlXPathSelector(response)
    #     i = HelloscrapyItem()
    #     #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
    #     #i['name'] = hxs.select('//div[@id="name"]').extract()
    #     #i['description'] = hxs.select('//div[@id="description"]').extract()
    #     return i
