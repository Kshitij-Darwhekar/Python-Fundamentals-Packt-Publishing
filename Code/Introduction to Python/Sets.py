# Sets in Python
# Sets are a collection of items that are stored in a variable. 
# They are unordered and unindexed. 
# No duplicate members.
# Sets are defined by curly brackets { } and items are separated by commas.
# Sets can contain any data type, including other sets.
# Sets can be accessed by their index, starting from 0.
# Sets can be modified by adding or removing items.
# Methods in Set --> set.add(), set.remove(), set.discard(), set.clear(), set.pop()

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")

print("Art Friends: ",art_friends)
print("Science Friends: ",science_friends)