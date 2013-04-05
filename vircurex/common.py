import json
import urllib
import httplib


domain = "vircurex.com"

api_schema = {
    "lowest_ask" : {
        "url" : "/api/get_lowest_ask.json",
        "return" : "value",
        "type" : float
    },
}


def request(api_call, params={}):
    api = api_schema[api_call]
     
    params = urllib.urlencode(params)
    url = "%s?%s" % (api["url"], params)
    
    connection = httplib.HTTPSConnection(domain)
    connection.request("GET", url, {}, {})
    response = connection.getresponse().read()
    connection.close()
    
    data = json.loads(response)
    value = data[api["return"]]
    return api["type"](value)

