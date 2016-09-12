#shell code: crul 'https://www.usenix.org/conference/usenixsecurity14/technical$
#this code is to get the urls of the target websites.

from bs4 import BeautifulSoup
soup = BeautifulSoup(open("/Users/Bruce/foo.html").read())
link = soup.findAll('h2', attrs={'class':'node-title clearfix'})
urls = []
abss = []
for n in link:
  url = 'https://www.usenix.org' + str(n.a['href'])
  urls.append(url)
       # name.a['href'] means find the attribute a(link).
techurl = [l for l in urls if "technical-sessions/presentation" in str(l)]

def AbsFinder(item_url)
  soup = BeautifulSoup(item_url)
  link = soup.findAll('div', {'class': 'field-item odd'})

