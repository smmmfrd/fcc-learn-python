users = ["Dave", "John", "Sara"]

data = ["Dave", 42, True]

emptylist = []

mylist = list([1, "Nel", True])
print(mylist)

# Prints boolean for if value is in list
print("Dave" in emptylist)

print(users[0])
print(users[-2])

# Index of value
print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(users))

users.append("Elsa")
print(users)

users += ["Jason"]
# users += "Jason"  # Since strings are arrays, it will add each character separately to the array
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

# Doesn't replace any, just adds to the array at this point
users[2:2] = ["Eddie", "Alex"]
print(users)

# Takes these indeces out and replaces them with these
users[1:3] = ["Heather", "Sam"]
print(users)

users.remove("Bob")
print(users)

# Get last value and return it
print(users.pop())
print(users)

del users[0]
print(users)

# del data 		# Remove from memory (bad)
data.clear()  # Clear it out
print(data)

print(users)
# Sorting places lowercase after upper.
users[1:2] = ["dave"]
users.sort()
print(users)

# Sorts prioritizing lowercase
users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

# Doesn't affect array
print(sorted(nums, reverse=True))
print(nums)

# Copy method
numscopy = nums.copy()

# Constructor
mynums = list(nums)

mycopy = nums[:]

print(nums)
numscopy.sort()
print("Pre-sorted: " + str(numscopy))
print(".sort(): " + str(mynums.sort()))
print(mycopy)

print(type(nums))
