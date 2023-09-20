# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst


def get_price(txt):
    return float(txt.replace('£', ''))

class EbookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = Field(
        output_processor = TakeFirst()
    )
    price = Field(
        input_processor = MapCompose(get_price),
        output_processor = TakeFirst()
    )


