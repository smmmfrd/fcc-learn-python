# Closure is a function having access to the scope of its parent function after the parent function has returned.

def parent_function(person, coins): # Params are closured on call.
	# Closured on call.
	# coins = 3

	def play_game():
		# Child func has parent function's var & it's changing value
		nonlocal coins
		coins -= 1

		if coins > 1:
			print(f"\n{person} has {coins} coins left.")
		elif coins == 1:
			print(f"\n{person} has {coins} coin left.")
		else:
			print(f"\n{person} is out of coins.")
	
	return play_game

tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()

jenny()

tommy()