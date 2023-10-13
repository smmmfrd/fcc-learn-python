from math import pi		# Only import one thing
import random as rdm	# Rename module
import kansas
from rps7 import rock_paper_scissors

print(pi)

print(rdm.random())

# Print all things in directory
# for item in dir(rdm):
# 	print(item)

print(kansas.capital)
kansas.randomfunfact()

print(__name__)			# Prints __main__ (the file being ran)
print(kansas.__name__)	# Prints kansas (name of file)

rock_paper_scissors()