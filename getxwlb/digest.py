# coding: UTF-8
# Keywords module
# To find and sort keywords in news content body

# from subprocess import *
import os
import csv

def gen_words(today):
    cmd = "rm " + today + "*.txt"
    os.system(cmd)
    cmd = "scrapy crawl xwlb"
    os.system(cmd)
    if os.stat(today+"-content.txt"):
        cmd = "scws -c utf8 -d /usr/local/etc/dict.utf8.xdb -t 50 -I -a ~r -i " + today + "-content.txt" + " > " + today + "-scwsout.txt"
        os.system(cmd)
    if os.stat(today+"-scwsout.txt"):
        fmt_words(today)
    if os.stat(today+"-keywords.txt"):
        cmd = "cat " + today+"-keywords.txt " + today+"-headline.txt " + today+"-content.txt " + " > " + today+"-final.txt"
        os.system(cmd)
    pass

def fmt_words(today):
    keywords = []
    for i, line in enumerate(open(today+"-scwsout.txt", 'r')):
        if i < 2:
            continue
        else:
            row = line.split()[:1] + ["\t\t\t"] + line.split()[-1:]
            #row = line.split()[:2] + line.split()[-1:]
            keywords.append(row)
    #print keywords
    with open(today+"-keywords.txt", 'wb') as f:
        writer = csv.writer(f, delimiter='\t', quotechar='|')
        writer.writerows(keywords)
    pass

if __name__ == "__main__":
    import sys
    gen_words(sys.argv[1])
    fmt_words(sys.argv[1])
