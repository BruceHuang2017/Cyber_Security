# this code is write to help me craw the abstract of essays in USENIX conference 2014.

import requests
from bs4 import BeautifulSoup

def AbstractFinder(abstra_url):
   source_code = requests.get(abstra_url)
   plain_text = source_code.text
   soup = BeautifulSoup(plain_text, "html5lib")
   for abstra_name in soup.findAll('div', {'class': 'field-item odd'}):
       print (abstra_name.string)

url = 'https://www.usenix.org/conference/usenixsecurity14/technical-sessions'

# I figure out the problem of this code is the url, the request returns and seems that the protocol is not supported.
# then I use another url say googel, and the code seems to work.

source_code = requests.get(url)
plain_text = source_code.text
#transation websourse to text version.
soup = BeautifulSoup(plain_text, "html5lib")
#conver to a bs object called soup.
for link in soup.findAll('a', {'class': 'node-title clearfix'}):
   href = 'https://www.usenix.org' + link.get('href')
   title = link.string
#only want text (string) inside the link
   print(href)
   print(title)
   AbstractFinder(href)
#find links of each essay or speech, 'a' means links in HTML.
