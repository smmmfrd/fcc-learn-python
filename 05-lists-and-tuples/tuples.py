# Tuples
mytuple = tuple(("Dave", 42, True))

anothertuple = (1, 4, 2, 8, 2, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

# Unpacking
(one, *two, hey) = anothertuple  # This * one takes the rest of the values
print(one)
print(two)
print(hey)

# Returns count of this value
print(anothertuple.count(2))
