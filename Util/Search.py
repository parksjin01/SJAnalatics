import urllib2
import BeautifulSoup

def Search(company):
    page = urllib2.urlopen('https://www.google.com/finance?q=%s&ei=gZpbWYCOJcqX0ASgwbSoAQ' %company).read()
    soup = BeautifulSoup.BeautifulSoup(page)
    tr = soup.findAll('tr', attrs={'class':'snippet'})
    result = []
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
        return -1
    return result

res = Search('Naver')
for line in res:
    print line