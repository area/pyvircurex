import time
import json
import urllib
import httplib
import hashlib


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
    },
    "balance" : {
        "url" : "/api/get_balance.json",
        "return" : "balance",
        "type" : float
    }
}


def make_request(api_call, params):
    api = api_schema[api_call]
     
    params = urllib.urlencode(params)
    url = "%s?%s" % (api["url"], params)
    
    connection = httplib.HTTPSConnection(domain)
    connection.request("GET", url, {}, {})
    response = connection.getresponse().read()
    connection.close()
    
    return json.loads(response)
   
   
def request(api_call, params={}):
    api = api_schema[api_call]
    data = make_request(api_call, params)

    if api.has_key("return"):
        value = data[api["return"]]
    else:
        value = data
    
    return api["type"](value)


def secure_request(account, api_call, token_string, names, params):
    api = api_schema[api_call]
    stamp, token = make_token(account, token_string["input"], params)
    request_params = {
        "account" : account.user,
        "id" : account.tid,
        "token" : token,
        "timestamp" : stamp,
    }
    request_params.update(zip(names, params))

    data = make_request(api_call, request_params)
    print data

    print check_token(account, data["timestamp"], token_string["output"], (data["balance"],))
  
    return api["type"](data["balance"])

     
def make_token(account, token_string, params):
    stamp = time.strftime("%Y-%m-%dT%H:%M:%S", tuple(time.gmtime()))
    params = tuple([account.secret, account.user, stamp, account.tid] + list(params))

    token = hashlib.sha256(token_string % params).hexdigest()
    return stamp, token


def check_token(account, stamp, token_string, params):
    params = tuple([account.secret, account.user, stamp] + list(params))

    print token_string % params
    token = hashlib.sha256(token_string % params).hexdigest()
    return  token

