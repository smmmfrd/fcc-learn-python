import math

print("")

# Integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Cast string to number
zip = "10001"
zip_value = int(zip)
print("Casted string of numbers type: " + str(type(zip_value)))

# Float
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# Complex (engineering)
# comp_value = 5 + 3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# Numeric Methods
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))  # Round with this amount after decimal

print("")

# Math methods!
print("math.pi" + "\t\t= " + str(math.pi))
print("math.sqrt(64)" + "\t= " + str(math.sqrt(64)))
print("math.ceil(3.28)" + "\t= " + str(math.ceil(gpa)))
print("math.floor(3.28)" + "= " + str(math.floor(gpa)))
