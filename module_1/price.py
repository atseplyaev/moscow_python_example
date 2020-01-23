def format_price(price):
    return "Цена: {} руб.".format(int(price))

price_str = format_price(56.24)

print(price_str)