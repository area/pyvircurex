import json
import httplib


domain = "https://vircurex.com/api/"
header = {"Content-type": "application/x-www-form-urlencoded"}


def request(url, params={}):
    connection = httplib.HTTPSConnection(domain)
    connection.request("POST", url, params, header)
    response = connection.getresponse().read()
    connection.close()

    return response

