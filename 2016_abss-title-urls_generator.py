from bs4 import BeautifulSoup
import urllib2

def abssFinder(furl):
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

def urlsFinder(urlf):
	urlf = urllib2.urlopen(urlf)
	soupf = BeautifulSoup(urlf.read())
	linkf = soupf.findAll('h2', attrs={'class': 'node-title clearfix'})
	urls = []
	for n in linkf:
		url = 'https://www.usenix.org' + str(n.a['href'])
		urls.append(url)
	techurl = [l for l in urls if "technical-sessions/presentation" in str(l)]
	return techurl

def titleFinder(furl):
	furl = urllib2.urlopen(furl)
	fsoup = BeautifulSoup(furl.read())
	flink = fsoup.findAll('h2', attrs={'class':'node-title clearfix'})
	titles = []
	for n in flink:
		url = 'https://www.usenix.org' + str(n.a['href'])
		if "technical-sessions/presentation" in url:
			text = n.text
			titles.append(text)
	return titles

if __name__=="__main__":

#input url need to analysis
url = 'https://www.usenix.org/conference/usenixsecurity14/technical-sessions'
#urls, titles as set, abss as dictionary.
urls = urlsFinder(url)
#want to get titles only without run abss code, save time. 
titles = titleFinder(url)
abss = abssFinder(url)
#if alrealy has the abss file, run the following code to get titles in a easier way. 
titles2 = abss.keys()

len(abss)
len(titles)
len(urls)
len(titles2)
