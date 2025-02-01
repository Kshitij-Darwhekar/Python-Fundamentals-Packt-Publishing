#Dectionaries in Oython
# A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.
# Dictionaries are used to store data values in key:value pairs.

friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print("Age of ROlf: ",friends_ages["Rolf"])

# Adding a new key-value pair
friends_ages["Bob"] = 20
# Here we are accessing the key in the dictionary and then assign a value to it.

#Dictionary are chnageable and indexed 
friends_ages["Rolf"] = 25
# Here we are changing the value of the key in the dictionary.

# But you can't have repeated keys in a dictionary
# friends_ages = {"Rolf": 24, "Rolf": 25}

print("Friends and their ages: ",friends_ages)

friends = (
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
)

print("Friends: ",friends)

print(friends[0]["name"])

# Dictionary Methods
# clear() --> Removes all the elements from the dictionary
# copy() --> Returns a copy of the dictionary
# fromkeys() --> Returns a dictionary with the specified keys and values
# get() --> Returns the value of the specified key
# items() --> Returns a list containing a tuple for each key value pair
# keys() --> Returns a list containing the dictionary's keys
# pop() --> Removes the element with the specified key
# popitem() --> Removes the last inserted key-value pair
# setdefault() --> Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update() --> Updates the dictionary with the specified key-value pairs

# Dict function
# dict() --> Converts to a dictionary

friends = [
    ("Rolf", 24),
    ("Adam", 30),
    ("Anne", 27)
]

friends_ages = dict(friends)
print("Friends and their ages: ",friends_ages)