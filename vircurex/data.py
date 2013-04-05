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
        pass

    @property
    def volume(self):
        pass

    @property
    def info(self):
        pass

    @property
    def orderbook(self):
        pass

    def trades(self, since):
        pass

