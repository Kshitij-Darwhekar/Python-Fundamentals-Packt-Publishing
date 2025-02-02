# Iterating over Dictionaries in Python
# Dictionaries are unordered collections of items

friend_ages = {
    "Rolf": 24,
    "Adam": 30,
    "Anne": 27
}

for name in friend_ages.keys():
    print(name)
# Here the code will print the keys of the dictionary

for age in friend_ages.values():
    print(age)
# Here the code will print the values of the dictionary

for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")
# Here the code will print the items of the dictionary
# The code will unpack the values from the dictionary into the variables
