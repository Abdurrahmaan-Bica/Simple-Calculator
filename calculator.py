from pyfiglet import Figlet





def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Can not divide by Zero!")
    else:
        return a / b


def power(base, exponent):
    return base ** exponent


