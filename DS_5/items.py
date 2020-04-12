# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class articleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    publish_date = scrapy.Field()
    article_url = scrapy.Field()
    content = scrapy.Field()
    categories = scrapy.Field()
    sources_url  = scrapy.Field()
    sources_wiki_page_url = scrapy.Field()
    scraped_at = scrapy.Field()
    # pass # not sure if needed