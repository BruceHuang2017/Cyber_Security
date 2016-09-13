from bs4 import BeautifulSoup
import urllib2


def urlFinder(furl):
	furl = urllib2.urlopen(str(furl))
	fsoup = BeautifulSoup(furl.read())
	flink = fsoup.findAll('h2', attrs={'class':'node-title clearfix'})
	abss = {}
	for n in flink:
		url = 'https://www.usenix.org' + str(n.a['href'])
		if "technical-sessions/presentation" in url:
			abs = absFinder(furl)	
			text = str(n.text)
			abss[text] = abs
	return abss

def absFinder(hurl):
	hurl = urllib2.urlopen(hurl)
	hsoup = BeautifulSoup(hurl.read())
	link = hsoup.findAll('div', {'class': 'field-item odd'})
	#figure out why there minus one. I think is related with the order. need to double check.
	testorder = len(link) - 1 
	return link[testorder].text

if __name__=="__main__":

#input url need to analysis
url = 'https://www.usenix.org/conference/usenixsecurity14/technical-sessions'
abss = urlFinder(url)
abss

