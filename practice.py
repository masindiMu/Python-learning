def add_num(a, b, c, d):
    """
    Function that add four numbers
    :param a: The first number to add
    :param b: The second number to add
    :param c: The third number to add
    :param d: The fourth number to add
    :return: None
    """
    total = a+ b + c +d
    return total


print(add_num(1, 2, 3, 4))
print(add_num(100, -200, 3745, 40))


def get_full_name():
    """
    Prompts the user to enter their names
    :return:
    """
    first_n = input("What is your first name?:")
    last_name = input("What is your last name?:")
    full_name = first_n + " " + last_name
    return full_name

full_name = get_full_name()
print(f"Hey, your full names are {full_name}")
print(full_name.upper())