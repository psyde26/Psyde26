def format_price(price):
    price = abs(int(price))
    result_price = "Цена:" + str(price) + "руб."
    return result_price


print(format_price(56.24))
