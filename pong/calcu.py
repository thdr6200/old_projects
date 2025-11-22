   
def add(*args):
    number = 0
    for i in args:
        number += i
    return number
def sub(*args):
    number = 0
    for i in args:
        number -= i
    return number
def mult(*args):
    number = 1
    for i in args:
        number *= i
    return number
def div(*args):
    try:
        number = 1
        for i in args:
            number /= i
        return number
    except ZeroDivisionError:
        return 