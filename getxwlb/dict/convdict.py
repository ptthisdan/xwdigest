#coding: UTF-8
import re

with open("cnmarket_utf8.txt", 'wb') as f:
    regex = re.compile('[a-zA-Z\']')
    for line in open('cn_market.txt', 'r'):
        line = line.decode(encoding='gb2312', errors='ignore').encode(
            encoding='utf-8', errors='strict'
        )
        f.write(regex.sub('', line))
    f.close()
