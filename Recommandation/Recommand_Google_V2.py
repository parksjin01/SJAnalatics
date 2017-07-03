import json
import urllib2
import re

def json_to_array(node):
    table = [['Company name', 'Symbol', 'Currency', 'Market cap', 'P/E ratio', 'Div yield (%)', '52w price change (%)']]
    for line in node['searchresults']:
        tmp = [0]*7
        tmp[0] = line['title']
        tmp[1] = line['ticker']
        tmp[2] = line['local_currency_symbol']
        tmp[3] = line['columns'][0]['value']
        tmp[4] = line['columns'][1]['value']
        tmp[5] = line['columns'][2]['value']
        tmp[6] = line['columns'][3]['value']
        table.append(tmp)
    return table

def Recommandation(num):
    original_page = urllib2.urlopen('https://www.google.com/finance?start=0&num='+str(num)+'&q=%5Bcurrency%20%3D%3D%20%22KRW%22%20%26%20((exchange%20%3D%3D%20%22KRX%22))%20%26%20(market_cap%20%3E%3D%200)%20%26%20(market_cap%20%3C%3D%20752680000000)%20%26%20(pe_ratio%20%3E%3D%200)%20%26%20(pe_ratio%20%3C%3D%2060054)%20%26%20(dividend_yield%20%3E%3D%200)%20%26%20(dividend_yield%20%3C%3D%2027330)%20%26%20(price_change_52week%20%3E%3D%200)%20%26%20(price_change_52week%20%3C%3D%202100000)%5D&restype=company&output=json&noIL=1&ei=gwdaWYLYNtef0ATQ-YqADw').read()
    page = []
    for line in original_page.split('\n'):
        line = re.sub(r'\\x[0-9A-Za-z][0-9A-Za-z]', ' ', line)
        page.append(line)
    page = '\n'.join(page)
    node = json.loads(page)
    node = json_to_array(node)
    return node