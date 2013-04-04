import json
import httplib


def request(url, params={}):
    header = {
        "Content-type": "application/x-www-form-urlencoded"
    }

    connection = httplib.HTTPSConnection(domain)
    connection.request("POST", url, params, header)
    response = connection.getresponse().read()
    connection.close()

    return response

