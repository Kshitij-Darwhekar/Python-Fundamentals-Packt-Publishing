# Advance set operations

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)

#difference() method returns a set that contains the difference between two sets.
#The returned set contains items that exist only in the first set, and not in both sets.
print("Art but not Science: ",art_but_not_science)
print("Science but not Art: ",science_friends.difference(art_friends))

not_in_both = art_friends.symmetric_difference(science_friends)
#symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.

print("Not in Both: ",not_in_both)

all_friends = art_friends.union(science_friends)
#union() method returns a set that contains all items from the original set, and all items from the specified sets.
print("All Friends: ",all_friends)
