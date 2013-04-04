
class Pair(object):
    def __init__(self, name):
        self.name = name

    @property
    def lowest_ask(self):
        pass

    @property
    def highest_bid(self):
        pass

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

