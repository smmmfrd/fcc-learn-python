person = "Sam"
coins = 3

print(f"\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)

player = {'person':'Sam', 'coins': 3, 'instrument': 'tuba'}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

# F-Strings, formats all values to strings & runs all code within then creates the string.
message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{player['person']} has {2*5} coins left."
print(message)

# Pass formatting
num = 10
print(f"\n2.25 times {num} is {(2.25 * num):.2f}\n") # .2 = min decimal places shown, f means floating point (Defaults to scientific notation)

for num in range(1,11):
	print(f"2.25 times {num} is {(2.25 * num):.2f}")

for num in range(1,11):
	print(f"{num} divided by 4.52 is {(num / 4.52):.2%}")

# Google more f string formatting types