import random

from common import secure_request, make_token


tokens = {
    "get_balance" : {
        # secret;user;timestamp;ID;get_balance;currency
        "input" : "%s;%s;%s;%i;get_balance;%s",
        # secret;user;timestamp;get_balance;balance
        "output" : "%s;%s;%s;get_balance;%s" 
    },
    "get_balances" : {
        # secret;user;timestamp;ID;get_balance
        "input" : "%s;%s;%s;%i;get_balances",
        # secret;user;timestamp;get_balance;balance
        "output" : "%s;%s;%s;get_balances;%s" 
    }
}


class Account(object):
    def __init__(self, user, secret):
        self.user = user
        self.secret = secret
        self.tid = random.randint(0, 2**32)

    def balance(self, currency):
        return secure_request(self, "balance",
                tokens["get_balance"], ("currency",), (currency,))


    def balances(self):
        pass
