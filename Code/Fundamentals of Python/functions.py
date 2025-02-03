# functions in Python
# Functions are a way to group a set of statements together.
# They are used to perform a specific task.
# Functions can take input parameters and return output values.

# Functions always start with the def keyword followed by the function name.
# The function name is followed by a set of parentheses that contain the input parameters.
# The function body is indented below the function definition.

def greet(name):
    print(f"Hello {name}")

name = input("Enter your name: ")    
greet(name)

# Output:
# Hello Alice
# Here name of the function is greet and it takes one input parameter name.

# Functions can also have multiple input parameters.
# Here is an example of a function that takes two input parameters.
def add_numbers(a, b):
    return a + b