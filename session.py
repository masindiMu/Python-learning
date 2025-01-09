#always have a docstring for our functions and write them in full sentences to explain the code
def greetings():
    """
    Greet the user
    :return: None
    """
    print("Hello")
    print("sawubona")
    print("Dumelang")

#Must have at least 2 lines after the function to call it out and you can call it as many
#times as you like
greetings()
greetings()


def multiples(x):
    """
    Multiples number by 5
    :param x: Number to be multiplied by 5
    :return: None
    """
    print(x * 5)

multiples(5)


def add_numbers(a, b, c, d):
    """
    Function that add four numbers
    :param a: The first number to add
    :param b: The second number to add
    :param c: The third number to add
    :param d: The fourth number to add
    :return: None
    """
    print(a+ b + c +d)

add_numbers(1, 2, 3, 4)
add_numbers(100, -200, 3745, 40)