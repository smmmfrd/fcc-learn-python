# Raise an error (not Throw)
class JustNotCoolError(Exception):
    pass


x = 2
try:
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")

    # This is a custom one, but we should normally use the standard ones.
    # raise Exception("I'm a custom exception!")

    raise JustNotCoolError("You're not cool enough.")
except NameError:
    print("NameError means something is undefined.")
except ZeroDivisionError:
    print("Dividing by zero? bruh...")
except Exception as error:
    print(error)
else:
    print("No errors")
finally:
    print("It's over.")
