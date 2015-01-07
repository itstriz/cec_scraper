import urllib2

def get_data(url):

    response = urllib2.urlopen(url)
    html = response.read()

    data_start = html.find("<td><p class=text>")
    data_end = html.find("</table>", data_start)
    all_results = html[data_start:data_end]
    
    print all_results
    return None


if __name__ == "__main__":
    cec_url = 'http://www.emergencyclosingcenter.com/ecc/home.jsp'
    get_data(cec_url)
