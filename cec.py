import urllib2

def get_data(url):
    response = urllib2.urlopen(url)
    html = response.read()

    data_start = html.find("<td><p class=text>")
    data_end = html.find("</table>", data_start)
    all_results = html[data_start:data_end]
    
    parse_data(all_results)

    return None

def get_facility_name(data, old_pos):
    start_search = "<p class=text>"
    end_search = "</p>"
    start_pos = data.find(start_search, old_pos)
    end_pos = data.find(end_search, start_pos)
        
    facility_name = data[start_pos + len(start_search):end_pos].strip()
    print facility_name

    while end_pos < len(data) and end_pos != -1:
        start_pos = data.find(start_search, end_pos + 1)
        end_pos = data.find(end_search, start_pos)

        if end_pos == -1:
            break

        facility_name = data[start_pos + len(start_search):end_pos].strip()

        print facility_name

    return facility_name
    
def parse_data(data):
    """ Parse data into a list """
    parsed_data = []

    # Find first bit of data
    get_facility_name(data, 0)

    return parsed_data

if __name__ == "__main__":
    cec_url = 'http://www.emergencyclosingcenter.com/ecc/home.jsp'
    get_data(cec_url)
