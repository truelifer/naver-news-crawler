# -*- coding: utf-8 -*-

from scrapy import Item, Field


class NaverNewsCrawlerItem(Item):
    id = Field()
    source = Field()
    category = Field()
    title = Field()
    editor = Field()
    created_date = Field()
    updated_date = Field()
    article = Field()
    images = Field()

    def initialize(self, value):
        for keys, _ in self.fields.items():
            self[keys] = value
