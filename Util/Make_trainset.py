# -*- encoding:utf-8 -*-

import random
import time
from Crawling.Crawl_Google import *
from Search import *

def get_code(num):
    page_num = (num/30)+1
    url = 'http://finance.daum.net/quote/marketvalue.daum?stype=P&page=%d&col=listprice&order=desc'
    result = []
    for i in range(1, page_num+1):
        page = urllib2.urlopen(url %(i)).read()
        soup = BeautifulSoup.BeautifulSoup(page)
        table = BeautifulSoup.BeautifulSoup(str(soup.findAll('table', attrs={'id':'tabSBody1'})))
        tmp = table.findAll('td')[5:]
        temp = tmp[::]
        tmp = []
        for node in temp:
            if node.text == '':
                continue
            tmp.append(node)
        for j in range(len(tmp)/8):
            result.append(tmp[j*8+1].text)

    return result[:num]

def make_set(num, duration):
    company_name = get_code(num)
    company = []
    done_list = []
    res = []
    idx = 1
    for one in company_name:
        print idx, one
        idx+=1
        if one in done_list:
            continue
        try:
            tmp = Search(one)
        except:
            print '[-] Error occured',one
            continue
        for i in tmp:
            company.append(i)
            done_list.append(i[0])
    idx = 0
    for info in company:
        try:
            res.append(crawl_stock(info[2], duration))
        except:
            print '[-] Error',idx
            idx += 1
        time.sleep(random.randint(1, 3))
    return res

print len(make_set(100, 60))