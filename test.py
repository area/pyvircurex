from vircurex import Pair


pair = Pair("btc_nmc")
print "ask: ", pair.lowest_ask
print "bid: ", pair.highest_bid
print "last: ", pair.last_trade
print "vol: ", pair.volume
print "info: ", pair.info
print "orderbook: ", pair.orderbook
print "trades since tid 196012: ", pair.trades(since=196012)

