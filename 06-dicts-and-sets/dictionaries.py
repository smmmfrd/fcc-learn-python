# Dictionaries
band = {"vocals": "Plant", "guitar": "Page"}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access
print(band["vocals"])
print(band.get("guitar"))

# List all ...
print(band.keys())
print(band.values())

# List all items as key/value tuples
print(band.items())

# Verify key
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JB"})
print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

# Pops last created item, returns a tuple!
print(band.popitem())
print(band)

band["drums"] = "Bonham"
print(band)
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries
# band2 = band  # Reference, not a copy.
# print(band)
# print(band2)

# band2["drums"] = "Dave"  # This gets applied to the first one
# print(band)

band2 = band.copy()  # Method
band2["drums"] = "Dave"
print(band)
print(band2)

band3 = dict(band)  # Constructor
band3["triangle"] = "Sam"
print(band)
print(band3)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals",
}
member2 = {
    "name": "Page",
    "instrument": "guitar",
}
band = {"member1": member1, "member2": member2}

print(band)
print(band["member1"]["name"])
