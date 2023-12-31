# String data type
print("")

# Literal assignment
print("Literal:")

first = "Sam"
last = "Mumford"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

print("")

# Constructor function
print("Constructor:")

pizza = str("Pepperoni")

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

print("")
# Concatenation
print("Concatenation:")

full_name = first + " " + last
print(full_name)

full_name += "!"
print(full_name)


print("")
# Casting a number to string
print("Casting:")

year = str(1995)
print(type(year))
print(year)

statement = "I was born in " + year + "."
print(statement)

# Multiple lines
multiline = """

Hey, how are ya?          

I'm checking in.
					All good?

"""
print(multiline)

# Escaping special characters
sentence = (
    "He said \"He didn't know nothing...\tabout nobody\"\nI didn't believe he\\him."
)
print(sentence)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

# Capitalize every word
print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

# Python counts whitespace.
print(len(multiline))
multiline += "                "
multiline = "                     " + multiline
print(len(multiline))

# Remove whitespace
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
# Build a menu
print("")
title = "menu".upper()

# Center within 20 characters, surrounded by equals signs
print(title.center(20, "="))

# Left justify coffee by 16 spaces and fill rest of it's spaces with periods, then right justify dollar amount with none of it's spaces taken up by any characer.
print("Coffee".ljust(16, ".") + "$1".rjust(4))

print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# String index values
print(first[0])
print(first[1])
print(first[-1])  # Final value
print(last[1:-1])  # Range of values (non-encapsulating)
print(last[1:])  # Range w/o ending goes to end
print(last[:-1])  # Range w/o start

# Boolean Methods
print(first.startswith("S"))
print(first.endswith("X"))
