PRICES = {"cola": 150, "chips": 100, "candy": 75}
COINS = [100, 50, 25, 10, 5]


def select_item(item, stock, credit):
    if item not in PRICES:
        return "invalid"
    if stock.get(item, 0) == 0:
        return "sold_out"
    if credit < PRICES[item]:
        return "insufficient"
    return "ok"


def make_change(amount):
    if amount < 0:
        raise ValueError("negative amount")
    coins = []
    for coin in COINS:
        while amount >= coin:
            coins.append(coin)
            amount -= coin
    if amount > 0:
        return None
    return coins


def purchase(item, stock, credit):
    status = select_item(item, stock, credit)
    if status != "ok":
        return status, []
    change = make_change(credit - PRICES[item])
    if change is None:
        return "no_exact_change", []
    stock[item] -= 1
    return "dispensed", change
