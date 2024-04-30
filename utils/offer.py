def percent_maker(price, percent):
    amount = price - ((price*percent) // 100)
    return amount
