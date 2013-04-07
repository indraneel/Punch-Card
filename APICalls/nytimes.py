import httplib
import simplejson as json

query = "bailout"
conn = httplib.HTTPConnection("api.nytimes.com")
url = "/svc/search/v1/article?query=" + query + "&api-key=ddabadc6f489ae99ad087f1892088d43:7:67526141"
conn.request("GET", url)
r = conn.getresponse()
data = r.read()
print data