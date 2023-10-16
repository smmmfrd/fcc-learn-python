def squared(num):
    return num * num


print(squared(2))

addTwo = lambda num: num + 2

print(addTwo(12))

sumTotal = lambda a, b: a + b

print(sumTotal(8, 7))


#########################


# Higher Order Function
def funcBuilder(x):  # Closures stores x here
    return lambda num: num + x  # Returns this lambda


# Creates the lambda, storing these values
addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

# And uses those
print(addTen(7))
print(addTwenty(7))


#########################


numbers = [3, 7, 12, 18, 20, 21]

squarednums = map(lambda num: num * num, numbers)
print(list(squarednums))


#########################

# Lambda returns true if num is odd
odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

#########################

from functools import reduce

sum_nums = reduce(lambda acc, curr: acc + curr, numbers, 10)
# Final arg is a starting value

print(sum_nums)

print(sum(numbers))

#########################


names = ["Rose Tyler", "The Doctor", "Mickey Baby"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
# Set the starting value to an int so the addition in the lambda can work.

print(char_count)
