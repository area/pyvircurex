from common import request


class Pair(object):
    def __init__(self, name):
        self.name = name
        self.base, self.alternate = self.name.split("_")

        self.default_params = {"base" : self.base.upper(),
                "alt" : self.alternate.upper()}

    @property
    def lowest_ask(self):
        return request("lowest_ask", self.default_params)

    @property
    def highest_bid(self):
        return request("highest_bid", self.default_params)

    @property
    def last_trade(self):
        return request("last_trade", self.default_params)

    @property
    def volume(self):
        return request("volume", self.default_params)

    @property
    def info(self):
        return request("info", self.default_params)

    @property
    def orderbook(self):
        return request("orderbook", self.default_params)

    def trades(self, since=None):
        params = self.default_params
        if since is not None:
            params["since"] = since
        return request("trades", params)

