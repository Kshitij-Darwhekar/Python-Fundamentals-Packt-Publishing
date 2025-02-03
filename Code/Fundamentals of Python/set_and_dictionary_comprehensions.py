# Sets and Dictionary Comprehensions in Python
# Sets and dictionary comprehensions are concise ways to create sets and dictionaries in Python.
# They are a compact way to write loops in Python.

numbers = [1, 2, 3, 4, 5]
even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)

# Output:
# {2, 4}

# Dictionary comprehension can also be used to create dictionaries.
# Here is an example of creating a dictionary with even numbers as keys and their squares as values.

friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
time_since_seen = [3,7,15,11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 10
}

print(long_timers) 

# Output:
# {'Alice': 15, 'Bob': 11}

# Dictionary comprehension can also be used to create tuples.
# Here is an example of creating a tuple with even numbers as elements.