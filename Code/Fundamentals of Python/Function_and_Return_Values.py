# Functions and Return Values in Python
# Functions are a way to group a set of statements together.
# They are used to perform a specific task.
# Functions can take input parameters and return output values.

def greet(name):
    return f"Hello {name}"

print(greet("Alice"))

# functions can return multiple values
def add_numbers(a, b):
    return a + b, a - b

result = add_numbers(3, 5)
print(result)

# Output:
# (8, -2)   