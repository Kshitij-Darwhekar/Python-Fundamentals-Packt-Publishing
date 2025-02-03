# Zip Function in Python
# The zip function is used to combine multiple lists into a single list of tuples.
# It takes multiple lists as arguments and returns a list of tuples.

friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
time_since_seen = [3, 7, 15, 11]

zipped_friends = zip(friends, time_since_seen)
print(list(zipped_friends))

# Output:
# [('Alice', 3), ('Bob', 7), ('Charlie', 15), ('David', 11), ('Eve', None)]

# We can have multiple lists zipped toghether 
# The zip function stops when the shortest list is exhausted

zipped_friends_and_time = zip(friends, time_since_seen, [1, 2, 3, 4, 5, 6, 7])
print(list(zipped_friends_and_time))

# Output:    
# [('Alice', 3, 1), ('Bob', 7, 2), ('Charlie', 15, 3), ('David', 11, 4)]

# Notice that the zip function only gives 4 tuples as the shortest list is of length 4
