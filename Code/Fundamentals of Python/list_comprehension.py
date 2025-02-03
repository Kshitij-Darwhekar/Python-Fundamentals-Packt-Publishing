# List Comprehension in Python
# List comprehension is a concise way to create lists in Python.
# It is a compact way to write loops in Python.

numbers = [1, 2, 3, 4, 5]
doubled_numbers = [x * 2 for x in numbers]
print(doubled_numbers)

# Output:
# [2, 4, 6, 8, 10]

# List comprehension can also be used to filter elements from a list.
# Here is an example of filtering even numbers from a list.

numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Output:
# [2, 4]

# List comprehension can also be used to create dictionaries.
# Here is an example of creating a dictionary with even numbers as keys and their squares as values.

numbers = [1, 2, 3, 4, 5]
even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
print(even_squares)

# Output:
# {2: 4, 4: 16}

# List comprehension can also be used to create tuples.
# Here is an example of creating a tuple with even numbers as elements.

numbers = [1, 2, 3, 4, 5]
even_tuple = tuple(x for x in numbers if x % 2 == 0)
print(even_tuple)

# Output:
# (2, 4)

# List comprehension can also be used to create sets.
# Here is an example of creating a set with even numbers.

numbers = [1, 2, 3, 4, 5]
even_set = {x for x in numbers if x % 2 == 0}
print(even_set)

# Output:
# {2, 4}
