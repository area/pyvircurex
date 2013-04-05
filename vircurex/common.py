import json
import urllib
import httplib


domain = "vircurex.com"


def request(url, params={}):
    params = urllib.urlencode(params)
    
    url = "%s?%s" % (url, params)
    
    connection = httplib.HTTPSConnection(domain)
    connection.request("GET", url, {}, {})
    response = connection.getresponse().read()
    connection.close()
    
    return response

