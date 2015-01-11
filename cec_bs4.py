from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.emergencyclosingcenter.com/ecc/home.jsp"

html = urlopen(BASE_URL).read()
soup = BeautifulSoup(html)

for table in soup.findAll('table'):
    if table.parent.name == 'td':
        data = table

for td in data.findAll('td'):
    if td.text.strip() != "":
        print td.text.strip()
