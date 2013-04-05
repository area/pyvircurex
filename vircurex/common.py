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
    "highest_bid" : {
        "url" : "/api/get_highest_bid.json",
        "return" : "value",
        "type" : float
    },
    "last_trade" : {
        "url" : "/api/get_last_trade.json",
        "return" : "value",
        "type" : float
    },
    "volume" : {
        "url" : "/api/get_volume.json",
        "return" : "value",
        "type" : float
    },
    "info" : {
        "url" : "/api/get_info_for_1_currency.json",
        "type" : dict
    },
    "orderbook" : {
        "url" : "/api/orderbook.json",
        "type" : dict
    },
    "trades" : {
        "url" : "/api/trades.json",
        "type" : list 
    }
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
    
    if api.has_key("return"):
        value = data[api["return"]]
    else:
        value = data
    
    return api["type"](value)

