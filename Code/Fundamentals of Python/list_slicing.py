# List slicing in Python
# List slicing is a way to access a subset of the list
# The syntax is list[start:end:step]
# Start is the index where the slice starts
# End is the index where the slice ends
# Step is the number of items to skip
# If you don't provide a start, it will default to 0

friends = ['Rolf', 'Jen', 'Bob', 'Anne', 'Mike', 'Jen']

print("Friends from 2 to 4: ")
print(friends[2:4])

print(friends[1:]) # From 1 to the end
print(friends[:4]) # From the start to 4
print(friends[:]) # All the list

print(friends[-3:]) # Last 3 elements
print(friends[:-2]) # All elements except the last 2

print(friends[1:-1]) # From 1 to the second last element

print(friends[1:-1:2]) # From 1 to the second last element, skipping 2 elements
