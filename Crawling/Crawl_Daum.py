import urllib2
import BeautifulSoup
import selenium


def crawl_stock_daily(code, num):
    url = 'http://finance.daum.net/item/quote_yyyymmdd_sub.daum?page=%d&code=%s&modify=0'
    page_num = (num / 30) + 1
    res = []
    for i in range(1, page_num+1):
        page = urllib2.urlopen(url % (i, code)).read()
        tmp = BeautifulSoup.BeautifulSoup(page).findAll('td')[1:]
        table = []
        for node in tmp:
            if node.text == '':
                continue
            table.append(node)
        for idx in range(len(table) / 8):
            res.append([table[idx * 8 + 4].text, '%s (%s)' % (table[idx * 8 + 5].text, table[idx * 8 + 6].text)])
    return res


def crawl_stock_timely(code, num):
    url = 'http://finance.daum.net/item/quote_hhmm.daum?page=%d&code=%s'
    page_num = (num / 30) + 1
    res = []
    for i in range(1, page_num + 1):
        page = urllib2.urlopen(url % (i, code)).read()
        tmp = BeautifulSoup.BeautifulSoup(page).findAll('td')[1:]
        table = []
        for node in tmp:
            if node.text == '':
                continue
            table.append(node)
        for idx in range(len(table) / 8):
            res.append([table[idx * 8 + 4].text, '%s (%s)' % (table[idx * 8 + 5].text, table[idx * 8 + 6].text)])
    return res


print crawl_stock_daily('005930', 20)
