from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.emergencyclosingcenter.com/ecc/home.jsp"

html = urlopen(BASE_URL).read()
soup = BeautifulSoup(html)

for table in soup.findAll('table'):
    if table.parent.name == 'td':
        data = table

closings = []
count = 0
for tr in data.findAll('tr'):
    school_name = tr.findAll('td')[1].text.strip()
    city = tr.findAll('td')[3].text.strip()
    status = tr.findAll('td')[5].text.strip()

    if school_name == "":
        school_name = closings[count - 1]['school_name']
        city = closings[count - 1]['city']

    closings.append({'school_name': school_name,
                     'city': city,
                     'status': status})     
    count = count + 1

for closing in closings:
    print "%s %s %s" % (closing['school_name'], closing['city'], closing['status'])
