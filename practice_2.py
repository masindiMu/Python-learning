def total_price(initial_price, tax_rate):
    """
    Calculate the total price after tax.
    :param initial_price: The price before tax
    :param tax_rate: The tax rate on the product
    :return: The price after tax.
    """
    price = initial_price + (initial_price * tax_rate/100)
    return price


def names(first_name):
    """
    Function that prints users first name in UPPERCASE and their last name in
    lowercase. The first name is an argument. The last name is retrieved from the
    user's input
    :param first_name: Users first name.
    :return: None
    """
    last_name = input("What is your last name?")
    print(first_name.upper() + " " + last_name.lower())


def summation(x, y):
    """
    Function that returns the sum of two argument
    :param x: The first value to add.
    :param y: The second value to add.
    :return: Sum of the two numbers.
    """
    return x+y
