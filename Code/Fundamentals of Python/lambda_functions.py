# Lambda Functions in Python
# Lambda functions are anonymous functions that can be defined in a single line.
# They are used to create small, one-off functions without the need for a full function definition.

def divide(x, y):
    return x / y

divide_by_2 = lambda x: x / 2

result = divide(10, 2)
print(result)

result = divide_by_2(10)
print(result)

# Output:
# 5
# 5.0

divide_y = lambda x, y: x / y

result = divide_y(10, 2)
print(result)

# Output:
# 5.0

# Using lambda function in a single line
print((lambda x,y: x/y)(10,2))

# Lamda functions can provide more simplicity to the code we can use them instead of defiing a full function

# Example

students = [
    {"name": "Alice", "grades": (67,90,95,100)},
    {"name": "Bob", "grades": (56,78,80,90)},
    {"name": "Charlie", "grades": (98,90,95,99)},
    {"name": "David", "grades": (100,100,95,100)},
    {"name": "Eve", "grades": (100,20,56,100)},
]

# Now we want to calucte the average grade for each student

average = lambda sequence: sum(sequence) / len(sequence)

for student in students:
    print(f"The average grade for {student['name']} is {average(student['grades'])}")


# Output:
# [78.0, 80.0, 95.0, 100.0, 100.0]
