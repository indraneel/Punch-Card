import httplib
import simplejson as json
import pystache 
import webbrowser

def get_stories(input):
    query = input 
    conn = httplib.HTTPConnection("api.nytimes.com")
    url = "/svc/search/v1/article?query=" + query + "&api-key=ddabadc6f489ae99ad087f1892088d43:7:67526141"
    conn.request("GET", url)
    r = conn.getresponse()
    data = r.read()
    return json.loads(data)

def generate_template(d):
    fo = open('../NYTelegram/index.html', 'rb')
    n = pystache.render(fo.read(),d)
    fo.close()
    out = open('../NYTelegram/output.html', 'wb+')
    out.write(n)
    out.close()
    webbrowser.open('file:///Users/indraneelpurohit/Dropbox/Punch-Card/NYTelegram/output.html')
    #fo = open('layout.html', 'w+')
    #fo.write("<!DOCTYPE html>\n")
    #fo.write("<html>")
    #fo.write(pystache.render('Date {{date}}!', d))
    #fo.close();

d = get_stories("north%20korea")
generate_template(d['results'][0])
