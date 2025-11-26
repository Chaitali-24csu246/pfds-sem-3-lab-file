# original dictionary
#this is not expt 13
d = {"brand": "Honda", "model": "Civic", "year": 2019}

print("Original dictionary:", d)

# length of dictionary
print("Length:", len(d))

# add an item
d["color"] = "Red"
print("After adding 'color':", d)

# remove an item
del d["model"]
print("After removing 'model':", d)

# create a copy
d_copy = d.copy()
print("Copy of dictionary:", d_copy)
