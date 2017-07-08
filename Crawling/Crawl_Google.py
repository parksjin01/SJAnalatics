# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import BeautifulSoup
import datetime
import time
import cPickle

def code_to_cid(stock_number):
    page = urllib2.urlopen('https://www.google.com/finance/historical?q=KRX%3A'+str(stock_number)+'&ei=SJdbWbjAHIva0QTMxYm4Bg')
    soup = BeautifulSoup.BeautifulSoup(page.read())
    cid = soup.findAll('input', attrs={'type':'hidden', 'name':'cid'})[0]
    return cid['value']

def crawl_stock(stock_number='', number_get=50, start_date=''):
    if start_date == '':
        start_date = datetime.datetime.now().strftime("%b %d %Y").split(' ')
        start_date[1] = str(int(start_date[1]))
        start_date = start_date[0]+'+'+start_date[1]+'%2C+'+start_date[2]
    if stock_number == '':
        assert 1==2
    cid = code_to_cid(stock_number)
    page = urllib2.urlopen('https://www.google.com/finance/historical?cid='+unicode(cid)+'&enddate='+unicode(start_date)+'&num='+unicode(number_get)+'&ei=WYVbWYCUI4va0QTMxYm4Bg').read()
    soup = BeautifulSoup.BeautifulSoup(page)
    page = str(soup.findAll('div', attrs={'id':'prices'})[0])
    table = []
    table_header = []
    soup = BeautifulSoup.BeautifulSoup(page)
    for th in soup.findAll('th'):
        table_header.append(th.text)
    table.append(table_header)
    table_contents = soup.findAll('td')
    for idx in range(0, len(table_contents)/6):
        tmp = [table_contents[idx*6].text, table_contents[idx*6+1].text, table_contents[idx*6+2].text, table_contents[idx*6+3].text, table_contents[idx*6+4].text, table_contents[idx*6+5].text]
        table.append(tmp)
    return table