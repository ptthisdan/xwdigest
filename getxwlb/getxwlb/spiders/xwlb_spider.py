# coding: UTF-8

import scrapy
import logging
from datetime import *
from bs4 import BeautifulSoup
import re

html_doc = """
<html>
    <head>
        <title>xwlb</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
<body>
"""

class XwlbSpider(scrapy.Spider):
    name = "xwlb"
    allowed_domains = ["cctv.cntv.cn", "tv.cctv.com"]
    start_urls = [
        "http://tv.cctv.com/lm/xwlb/index.shtml"
    ]
    filename = date.today().strftime('%Y%m%d')
    filter=re.compile('\[视频\]|\(新闻联播\)')
    headline_file = open(filename+"-headline.txt", 'w')
    headline_file.close()

    def parse(self, response):
        logging.info(response.url)
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            if u'2016' in link[0]:
                with open(self.filename+"-headline.txt", 'a') as txt:
                    #txt.write('\n----------------------------------\n'.encode('UTF-8'))
                    headline = self.filter.sub('', title[0].encode('UTF-8'))
                    #print headline
                    txt.write(headline)
                    txt.close()
                print link[0]
                yield scrapy.Request(link[0], callback=self.parse_today_contents)

    def parse_today_contents(self, response):
        with open(self.filename+"-content.txt", 'a') as txt:
            txt.write('\n----------------------------------\n'.encode('UTF-8'))
            for sel in response.xpath('//div[@class="cnt_bd"]/p/text()'):
                txt.write('\n'.encode('UTF-8'))
                t = sel.extract()
                content = self.filter.sub('', t.encode('UTF-8'))
                txt.write(content)
            txt.close()
