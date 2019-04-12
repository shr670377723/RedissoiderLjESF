# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from lianjia.items import LianjiaItem
from scrapy_redis.spiders import RedisSpider

class PlianjiaSpider(RedisSpider):
    name = 'plianjia'
    # allowed_domains = ['lianjia.com']
    # start_urls = ['https://bj.lianjia.com/ershoufang/']

    base_url = 'https://bj.lianjia.com/ershoufang/pg{}/'
    redis_key = 'lianjia:start_urls'
    index = 1
    def parse(self, response):

        html = response.xpath("//a[@class='title']/@href").extract()
        for i in html:
            yield scrapy.Request(i,callback=self.info_lj,dont_filter=True)
        if self.index<=100:
            self.index += 1
            yield  scrapy.Request(self.base_url.format(self.index),callback=self.parse,dont_filter=True)

    def info_lj(self,response):

        roomname = response.xpath("//h1/text()").extract_first()
        price = response.xpath("concat(//div[@class='price ']/span[1],//div[@class='price ']/span[2])").extract_first()
        huxing = response.xpath("//div[@class='base']/div[@class='content']/ul/li[1]/text()").extract_first()
        louceng = response.xpath("//div[@class='base']/div[@class='content']/ul/li[2]/text()").extract_first()
        mianji = response.xpath("//div[@class='base']/div[@class='content']/ul/li[3]/text()").extract_first()
        jiegou = response.xpath("//div[@class='base']/div[@class='content']/ul/li[4]/text()").extract_first()
        zhuangxiu = response.xpath("//div[@class='base']/div[@class='content']/ul/li[9]/text()").extract_first()
        gongnuan = response.xpath("//div[@class='base']/div[@class='content']/ul/li[11]/text()").extract_first()
        dianti = response.xpath("//div[@class='base']/div[@class='content']/ul/li[12]/text()").extract_first()
        chanquan = response.xpath("//div[@class='base']/div[@class='content']/ul/li[13]/text()").extract_first()

        quanshu  = response.xpath("//div[@class='transaction']/div[@class='content']/ul/li[2]/span[2]/text()").extract_first()
        nianxian = response.xpath("//div[@class='transaction']/div[@class='content']/ul/li[5]/span[2]/text()").extract_first()
        diya = response.xpath("//div[@class='transaction']/div[@class='content']/ul/li[7]/span[2]/text()").extract_first().strip()

        item = LianjiaItem()
        item['roomname'] = roomname
        item['price'] = price
        item['huxing'] = huxing
        item['louceng'] = louceng
        item['mianji'] = mianji
        item['jiegou'] = jiegou
        item['zhuangxiu'] = zhuangxiu
        item['gongnuan'] = gongnuan
        item['dianti'] = dianti
        item['chanquan'] = chanquan

        item['quanshu'] = quanshu
        item['nianxian'] = nianxian
        item['diya'] = diya
        yield item


