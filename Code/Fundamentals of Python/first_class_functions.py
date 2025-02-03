# First Class Functions in Python
# First class functions are functions that can be assigned to variables and passed as arguments to other functions.
# They are used to create functions that can be used in different contexts.

# def add(x, y):
#     return x + y

# add = add() # Here we didn't use the brackets so we did not call the function we just assigned it to a variable

# print(add(5, 3))

# Output:
# 5

# We can assign a function to another function

def before_and_after(func):
    print("Before")
    func()
    print("After")
    
def greet():
    print("Hello")

before_and_after(greet) # Here we are not callin the greet function
# We are passing the greet function

# this will be more important in decorators

# Higher order functions
# Higher order functions are functions that take other functions as arguments or return functions as output.
# They are used to create functions that can be used in different contexts.

operations ={
    "average": lambda sequence: sum(sequence) / len(sequence),
    "total": lambda sequence: sum(sequence),
    "top": lambda sequence: max(sequence)
                                
}

students = [
    {"name": "Alice", "grades": (67,90,95,100)},
    {"name": "Bob", "grades": (56,78,80,90)},
    {"name": "Charlie", "grades": (98,90,95,99)},
    {"name": "David", "grades": (100,100,95,100)},
    {"name": "Eve", "grades": (100,20,56,100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]
    operation = input(f"Enter the operation for {name} (average/total/top): ")
    
    result = operations[operation](grades)
    print(result)