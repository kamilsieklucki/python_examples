# example of using dict ----------------------------------------
# Declare a dict
student = {'name': 'John', 'age': 14}
# Get a value
age = student['age']
# age is 14
# Update a value
student['age'] = 15
# student becomes {'name': 'John', 'age': 15}
# Insert a key-value pair
student['score'] = 'A'
# student becomes {'name': 'John', 'age': 15, 'score': 'A'}

# example data for union dict problem --------------------------
# two dicts to start with
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d2a = {'a': 10, 'c': 3, 'd': 4}
# target dict
d3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using the update() method ------------------------------------
# create a copy of d1, as update() modifies the dict in-place
d3 = d1.copy()
# d3 is {'a': 1, 'b': 2}
# update the d3 with d2
d3.update(d2)
# d3 now is {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d3)

d3 = d1.copy()
d3.update(d2a)
# d3 now is {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# This is not the way that we want
print(d3)
d3 = d2a.copy()
d3.update(d1)
# d3 now is {'a': 1, 'c': 3, 'd': 4, 'b': 2}
# This is the way that we want
print(d3)

# Unpacking dictionaries -------------------------
# unpacking
d3 = {**d1, **d2a}
# d3 is {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# Not right
print(d3)
d3 = {**d2a, **d1}
# d3 is {'a': 1, 'c': 3, 'd': 4, 'b': 2}
# Good
print(d3)

# Using dict(iterable, **kwarg) ------------------
d3 = dict(d1, **d2)
# d3 is {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Good, it's what we want
print(d3)
d3 = dict(d1, **d2a)
# d3 is {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# Not right, 'a' value got replaced
print(d3)
# in this method key must be a string !!!
dict({'a': 1}, **{2: 3})
dict({'a': 1}, **{'2': 3})

# Merging Dictionaries since Python 3.9.0a4 ---------------
# use the merging operator |
d3 = d1 | d2
# d3 is now {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# good
d3 = d1 | d2a
# d3 is now {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# not good

# Create a copy for d1
d3 = d1.copy()
# Use the augmented assignment of the merge operator
d3 |= d2
# d3 now is {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# good
d3 |= d2a
# d3 now is {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# not good

