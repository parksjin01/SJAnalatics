# -*- encoding:utf-8 -*-

import random
import time
from Crawling.Crawl_Google import *
from Crawling.Crawl_Daum import *
import threading
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

def trimming(original, idx=0):
    result = []
    for company in original:
        tmp = []
        for day in company:
            tmp.append(day[idx])
        result.append(tmp)
    return result



def crawling_with_google(company, duration, res):
    idx = 0
    tmp = []
    for info in company:
        if idx%100 == 0:
            time.sleep(5)
        try:
            idx += 1
            tmp.append(crawl_stock(info[2], duration)[1:])
        except:
            print threading.current_thread(), idx
            continue
    res.append(tmp)
    res.append(trimming(tmp, -2))

def crawling_with_daum(company, duration, res):
    idx = 0
    tmp = []
    for info in company:
        try:
            idx += 1
            tmp.append(crawl_stock_daily(info[2], duration))
        except:
            print threading.current_thread(), idx
            continue
    res.append(tmp)
    res.append(trimming(tmp, 0))

def make_set(num, duration):
    company_name = get_code(num)
    company = []
    done_list = []
    idx = 1
    for one in company_name:
        print idx, one
        idx+=1
        if one in done_list:
            continue
        try:
            tmp = Search(one)
        except Exception, e:
            print e
            print '[-] Error occured',one
            continue
        for i in tmp:
            company.append(i)
            done_list.append(i[0])
    res = [[], [], [], []]

    thread1 = threading.Thread(target=crawling_with_google, name='thread1',
                               args=[company[:int(len(company)*0.25)], duration, res[0]])
    thread2 = threading.Thread(target=crawling_with_google, name='thread2',
                               args=[company[int(len(company)*0.25):int(len(company)*0.5)], duration, res[1]])
    thread3 = threading.Thread(target=crawling_with_daum, name='thread3',
                               args=[company[int(len(company) * 0.5):int(len(company) * 0.75)], duration, res[2]])
    thread4 = threading.Thread(target=crawling_with_daum, name='thread4',
                               args=[company[int(len(company) * 0.75):], duration, res[3]])

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    res = res[0]+res[1]+res[2]+res[3]
    res = [res[1], res[3], res[5], res[7], res[0], res[2], res[4], res[6]]
    with open('dataset', 'wb') as f:
        cPickle.dump(res, f)

make_set(1000, 300)
# print crawl_stock('005930', 60)
# print crawl_stock_daily('005930', 60)