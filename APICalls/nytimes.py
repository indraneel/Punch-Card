import httplib

conn = httplib.HTTPConnection("api.nytimes.com")
conn.request("GET", "/svc/search/v1/article?query=bailout&api-key=ddabadc6f489ae99ad087f1892088d43:7:67526141")
r = conn.getresponse()
data = r.read()
print data