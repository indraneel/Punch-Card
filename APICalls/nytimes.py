import httplib
import simplejson as json
import pystache 
import webbrowser
import unicodedata

def get_stories(input):
    query = input 
    conn = httplib.HTTPConnection("api.nytimes.com")
    url = "/svc/search/v1/article?query=" + query + "&api-key=ddabadc6f489ae99ad087f1892088d43:7:67526141"
    conn.request("GET", url)
    r = conn.getresponse()
    data = json.loads(r.read())
    # keys = ['tit{}'.format(i) for i in range(0,3)]
    # titles = []
    # for i in range(0,3):
    #     tit = data['results'][i]['title']
    #     if (not isinstance(tit, str)):
    #         tit = unicodedata.normalize('NFKD', tit).encode('ascii','ignore')
    #     titles.append(tit)
    # titles = data['results'][i]['title'] for i in range(0,3)
    # d = dict(zip(keys, titles))
    # print d

    return {'body': data['results'][0]['body']}

def generate_template(d):
    fo = open('../NYTelegram/index.html', 'rb')
    n = pystache.render(fo.read(),d)
    fo.close()
    out = open('../NYTelegram/output.html', 'wb+')
    out.write(n)
    webbrowser.open_new('file:\\\\C:\Users\mattmik\Documents\HackNY\Punch-Card\NYTelegram\output.html')
    out.close()
	
    # webbrowser.open('file:///Users/indraneelpurohit/Dropbox/Punch-Card/NYTelegram/output.html')
    #webbrowser.open_new_tab('file:///Users/lavi/Documents/Git Repos/Punch-Card/NYTelegram/output.html')
    #fo = open('layout.html', 'w+')
    #fo.write("<!DOCTYPE html>\n")
    #fo.write("<html>")
    #fo.write(pystache.render('Date {{date}}!', d))
    #fo.close();

#d = get_stories("google")
#generate_template(d)
