# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    roomname = scrapy.Field()

    price = scrapy.Field()
    huxing = scrapy.Field()
    louceng = scrapy.Field()
    mianji = scrapy.Field()
    jiegou = scrapy.Field()
    zhuangxiu = scrapy.Field()
    gongnuan = scrapy.Field()
    dianti = scrapy.Field()
    chanquan = scrapy.Field()

    quanshu = scrapy.Field()
    nianxian = scrapy.Field()
    diya = scrapy.Field()


