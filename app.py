class MyCustomErr (Exception):
    pass


def divide(a, b):
    if b == 0:
        raise MyCustomErr("Cannot Divide By Zero")

    return a / b


num1 = int(input("please enter a number : "))
num2 = int(input("please enter a number : "))

print(divide(num1, num2))
