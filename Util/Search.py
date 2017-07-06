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

def Search(company):
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

res = Search('shinhan')
for line in res:
    if line[1] == u'KRX':
        print '"'+line[2]+'",',