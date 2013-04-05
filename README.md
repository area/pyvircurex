Trade cryptocurrencies on the [vircurex](http://vircurex.com) exchange quickly and easily.

##Usage

Public tick data for all available pairs can be accessed like this:

    from vircurex import Pair

    pair = Pair("btc_nmc")
    pair.lowest_ask
    pair.highest_bid
    pair.last_trade
    pair.volume
    pair.orderbook
    pair.trades(since=196012) # since nominated tick ID

Trading is just as easy:

    from vircurex import Account
    
    account = Account("username", "api_secret")
    account.balance("BTC")

    # Create an order, returns a dict
    order = account.buy("NMC", 1, "BTC", 0.001) # buy 1 NMC at a price of 0.001 BTC
    account.delete(order["orderid"])

# TODO

Vircurex allows for difference secrets for different API calls, presently this wrapper assumes all API calls have the same secret.
