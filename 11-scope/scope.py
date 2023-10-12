name = "Sam" # Global scope
count = 1

# greeting("Sbeve")

def another():
	color = "blue" # Local scope

	# Can't modify global variable in local scope
	# count += 2

	# Have to do this to create reference to global var
	global count
	count += 1
	print(count)

	# Locally scoped variable
	def greeting(name): # Same name as global scope, but local.
		# Say that we're using a higher scoped variable
		nonlocal color
		color = "red"
		print(name)
		print(color)
	
	greeting("Aurelia")

another()
print(count)