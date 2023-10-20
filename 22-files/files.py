# r - Read
# a - Append
# w - Write
# x - Create
# (CRUD but for python I guess)

import os

# Read - errs if !exists
f = open("names.txt", "r")  # don't need the second arg
# print(f.read())
# print(f.read(4))

# print(f.readline())  # Prints everything including the \n in the line
# print(f.readline()) # Prints next line

for line in f:
    print(line)

# Changes don't apply until closed.
f.close()

# Append
f = open("names.txt", "a")
f.write("\nSam")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("DELETE")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Create new file

# Opens a file for writing & if !exists, creates it
f = open("name_list.txt", "w")
f.close()

# Creates the file, but returns an err if file exists.
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist.")

# The real way!
with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
