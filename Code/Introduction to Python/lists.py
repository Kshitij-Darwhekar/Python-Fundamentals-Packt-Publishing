# Lists in Python
# Lists are a collection of items that are stored in a variable. They are ordered and changeable. Allows duplicate members.
# Lists are defined by square brackets [ ] and items are separated by commas.
# Lists can contain any data type, including other lists.
# Lists can be accessed by their index, starting from 0.
# Lists can be modified by adding or removing items.
# Methods in List --> list.append(), list.remove(), list.pop(), list.clear(), list.sort(), list.copy(), list.reverse()

friends = ["Rolf", "Bob", "Anne"]

print(friends[0])
print(friends[1])

friends2 = [
    ["Rolf", 24],
    ["Bob", 30],
    ["Anne", 27]
]

print(friends2[0][0])

friends.remove("Bob")

friends.append("Jen")

print(friends)