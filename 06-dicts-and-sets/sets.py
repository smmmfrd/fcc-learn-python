# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(type(nums2))
print(len(nums))

# No duplicates allowed
nums = {1, 2, 2, 3}
print(nums)  # prints {1, 2, 3}

# True is dupe of 1, False is 0, takes whichever is placed first
nums2 = {0, True, False, 1}
print(nums2)

# Check if value is in set
print(2 in nums)

# Can't do index or key

# Add element
nums.add(8)  # Adds to front?
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep except dupes
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
