# Join in Python
# join() --> Joins the elements of an iterable to the end of the string

friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
# This will take different values in the list 
# and join them with the string provided in the join method. (here a comma)
print("My friends are: ",comma_separated)

print("My friends in list are: ",friends)

print(type(comma_separated))