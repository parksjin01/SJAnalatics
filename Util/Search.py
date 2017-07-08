# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import BeautifulSoup

def search_onecompany(page):
    soup = BeautifulSoup.BeautifulSoup(page)
    company_header = BeautifulSoup.BeautifulSoup(str(soup.findAll('div', attrs={'id':'companyheader'})[0]))
    body = BeautifulSoup.BeautifulSoup(str(soup.findAll('div', attrs={'id':'market-data-div'})[0]))
    last_price = body.findAll('span', attrs={'class':'pr'})[0]
    quote_change = body.findAll('span', attrs={'class':'ch bld'})[0]
    mkt_cap = BeautifulSoup.BeautifulSoup(str(BeautifulSoup.BeautifulSoup(str(body.findAll('table', attrs={'class':'snap-data'})[0])).findAll('tr')[4])).findAll('td')[1]
    company_name, _, company_ticket = company_header.text.split('&nbsp;')[:3]
    exchange, company_ticket = company_ticket.split(', ')[1].strip(')').split(':')
    return [company_name, exchange, company_ticket, last_price.text, quote_change.text, mkt_cap.text]

def Search_Google(company):
    page = urllib2.urlopen('https://www.google.com/finance?q=%s&ei=gZpbWYCOJcqX0ASgwbSoAQ' %company).read()
    soup = BeautifulSoup.BeautifulSoup(page)
    result = []
    tr = soup.findAll('tr', attrs={'class':'snippet'})
    for line in tr:
        soup = BeautifulSoup.BeautifulSoup(str(line))
        tmp = []
        if soup.findAll('td', attrs={'class':'exch'}) != []:
            if soup.findAll('td', attrs={'class':'exch'})[0].text == 'KRX':
                td = soup.findAll('td')
                for node in td:
                    tmp.append(node.text)
                result.append(tmp)
    if result == []:
        result.append(search_onecompany(page))
    if result == []:
        return -1
    return result

def Search_Daum(company):
    base_url = 'http://finance.daum.net/'
    url = 'http://finance.daum.net/search/search.daum?page=1&col=hname&order=desc&name=%s&nil_stock=refresh'
    page = urllib2.urlopen(url %company).read()
    result = []
    if 'tabSBody1' in page:
        soup = BeautifulSoup.BeautifulSoup(page)
        company = BeautifulSoup.BeautifulSoup(str(soup.findAll('table', attrs={'id':'tabSBody1'})[0]))
        line = company.findAll('tr')[2:]
        for one in line:
            try:
                a = BeautifulSoup.BeautifulSoup(str(one)).findAll('a')[0]
            except:
                continue
            new_page = urllib2.urlopen(base_url+a['href'])
            title = str(BeautifulSoup.BeautifulSoup(new_page).findAll('div', attrs={'id':'topWrap'})[0])
            if u'코스피' in title:
                tmp = BeautifulSoup.BeautifulSoup(str(one)).findAll('td')
                result.append([tmp[1].text, 'KRX', BeautifulSoup.BeautifulSoup(title).findAll('span', attrs={'class':'stockCode'})[0].text, tmp[2].text, '%s (%s)' %(tmp[3].text, tmp[4].text), 'NaN'])
    else:
        info = BeautifulSoup.BeautifulSoup(str(BeautifulSoup.BeautifulSoup(page).findAll('div', attrs={'id':'topWrap'})[0]))
        price = BeautifulSoup.BeautifulSoup(str(info.findAll('ul', attrs={'class':'list_stockrate'})[0])).findAll('li')
        result.append([company, 'KRX', info.findAll('span', attrs={'class':'stockCode'})[0].text, price[0].text, '%s (%s)' %(price[1].text, price[2].text), 'NaN'])
    return result

def Search(company, potal="daum"):
    if potal.lower() == "daum":
        return Search_Daum(company)
    else:
        return Search_Google(company)
