def hello_world(target):
    print("Hello " + str(target) + "!")


hello_world("mom")


def sum(num1=0, num2=0):  # default param values
    # print(num1 + num2)
    # Escape condition
    if type(num1) is not int or type(num2) is not int:
        return

    return num1 + num2


# sum(1, 2)
# sum(3, 2)
# sum(9, 7)
# sum(18, 7)

total = sum(18, 7)
print(total)

strtotal = sum("Hello ", "world!")  # returns none
print(strtotal, type(strtotal))  # type is NoneType

defaulttotal = sum(1)
print(defaulttotal)


def mutliple_items(*args):
    # Undefined number of parameters come in as a tuple
    print(args, type(args))


mutliple_items("Dave", "John", "Sarah")


def mult_named_items(**kwargs):  # keyworded arguments
    print(kwargs, type(kwargs))  # kwargs come in as dictionary


mult_named_items(first="Sam", last="Mumford")
