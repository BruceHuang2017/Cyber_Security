from bs4 import BeautifulSoup
import urllib2
urlf = urllib2.urlopen('https://www.usenix.org/conference/usenixsecurity14/technical-sessions')
# check by : print page
soup = BeautifulSoup(urlf.read())
link = soup.findAll('h2', attrs={'class':'node-title clearfix'})

urls = []
for n in link:
	url = 'https://www.usenix.org' + str(n.a['href'])
	urls.append(url)
techurl = [l for l in urls if "technical-sessions/presentation" in str(l)]

def AbsFinder(testurl):
    testurlf = urllib2.urlopen(testurl)
    testsoup = BeautifulSoup(testurlf.read())
    link = testsoup.findAll('div', {'class': 'field-item odd'})
    testorder = len(link) - 1
    return link[testorder].text

abss = []
for m in techurl:
    abs = AbsFinder(m)
    abss.append(abs)

