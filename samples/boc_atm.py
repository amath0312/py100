# -*- coding:utf8 -*-
import urllib.request as request
from bs4 import BeautifulSoup

baseurl = 'http://www.bankofchina.com/sourcedb/atmdist/406/678/681/index%s.html'

in_bank = 0
out_bank = 0
for i in range(20):
    if i == 0:
        url = baseurl%''
    else:
        url = baseurl % ('_'+str(i))
    print("i = %d, url = %s" % (i,url))
    req = request.Request(url)
    resp = request.urlopen(req, timeout=100)
    data = resp.read().decode('utf-8')
    soup = BeautifulSoup(data, 'lxml')
    banks = soup.select('#documentContainer')[0].get_text()
    print(banks)
    in_bank = in_bank + banks.count('依附')
    out_bank = out_bank + banks.count('离行')

print('离行式：%d' % out_bank)
print('在行式：%d' % in_bank)
print('离行式占比：%s %%' % round(out_bank * 100 / in_bank,2))
