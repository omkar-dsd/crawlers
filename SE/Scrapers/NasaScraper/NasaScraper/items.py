# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class NasascraperItem(Item):
    # define the fields for your item here like:
    # name = Field()
    URL = Field()
    Phase = Field()
    Launch_Date = Field()
    Content = Field()
    pass
