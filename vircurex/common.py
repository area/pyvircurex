import json
import urllib
import httplib


domain = "vircurex.com"
header = {"Content-type": "application/x-form-urlencoded",
        "Accept": "text/plain"}


def request(url, params={}):
    params = urllib.urlencode(params)

    connection = httplib.HTTPSConnection(domain)
    connection.request("POST", url, params, header)
    response = connection.getresponse().read()
    connection.close()

    return response

