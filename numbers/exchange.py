def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget/exchange_rate
    
print(exchange_money(127.5, 1.2))

def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    
    return budget - exchanging_value

print(get_change(127.5, 120))

def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills

print(get_value_of_bills(5, 128))

def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination

print(int(get_number_of_bills(127.5, 5)))

def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget - get_number_of_bills(budget, denomination)*denomination

print(get_leftover_of_bills(127.5, 20))


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    
    new_exchange_rate = exchange_rate *(1 + spread / 100)
    budget_exchanged = exchange_money(budget, new_exchange_rate)    

    return int(get_number_of_bills(budget_exchanged, denomination)*denomination)


print(exchangeable_value(127.25, 1.20, 10, 20))

print(exchangeable_value(127.25, 1.20, 10, 5))

