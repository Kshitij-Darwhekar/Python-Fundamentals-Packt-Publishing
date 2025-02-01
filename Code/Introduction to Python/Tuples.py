# Tuples in Python
# Tuples are a collection of items that are stored in a variable. They are ordered and unchangeable. Allows duplicate members.
# Tuples are defined by parentheses ( ) and items are separated by commas.
# Tuples can contain any data type, including other tuples.
# Tuples can be accessed by their index, starting from 0.
# Tuples can be modified by adding or removing items.
# Methods in Tuple --> tuple.count(), tuple.index()

short_tuple = ("Rolf" , "Bob" , "Anne")

# They can also be written as
short_tuple = "Rolf" , "Bob" , "Anne"

print("Short Tuple: ",short_tuple)

tuple_in_list = [("Ross","Phoebe"),"Chandler"]

print("Tuple in List: ",tuple_in_list)

# Difference between List and Tuple
# List is mutable, Tuple is immutable (Meaning you can't change the values in a tuple)
# You can add two tuples together

# Tuple Methods
# count() --> Returns the number of times a specified value occurs in a tuple
# index() --> Searches the tuple for a specified value and returns the position

print("Count: ",short_tuple.count("Rolf"))
print("Index: ",short_tuple.index("Bob"))

