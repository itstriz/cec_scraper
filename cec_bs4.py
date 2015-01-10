from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.emergencyclosingcenter.com/ecc/home.jsp"

html = urlopen(BASE_URL).read()
soup = BeautifulSoup(html)
items = soup.findAll("p", {"class": "text"})

for item in items:
    print item.text
