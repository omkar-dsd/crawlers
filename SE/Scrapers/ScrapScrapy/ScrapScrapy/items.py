# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrapscrapyItem(Item):
    # define the fields for your item here like:
    # name = Field()

    Heading = Field()
    Content = Field()
    Source_Website = Field()

    #storing the things that we are gonna scrape
    
    pass
