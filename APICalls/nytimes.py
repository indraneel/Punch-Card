import httplib
import simplejson as json
import pystache 

def get_stories(input):
    query = input 
    conn = httplib.HTTPConnection("api.nytimes.com")
    url = "/svc/search/v1/article?query=" + query + "&api-key=ddabadc6f489ae99ad087f1892088d43:7:67526141"
    conn.request("GET", url)
    r = conn.getresponse()
    data = r.read()
    return json.loads(data)

def generate_template(d):
    print pystache.render('Date {{date}}!', d) 


d = get_stories("north%20korea")
generate_template(d['results'][0])
