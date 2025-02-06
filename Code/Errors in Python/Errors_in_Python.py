# Errors in Python
# How we can use them, how we can handle them

# IndexError --> Happens when we try to access an element of a list or a string that does not exist

my_list = [1, 2, 3, 4, 5]

print(my_list[6]) # IndexError


# KeyError --> Happens when we try to access a dictionary that does not exist

my_dict = {'a': 1, 'b': 2, 'c': 3}

print(my_dict['d']) # KeyError


# NameError --> Happens when we try to access a variable that does not exist

print(non_existent_variable) # NameError


# AttributeError --> Happens when we try to access an attribute that does not exist

class MyClass:
    pass

my_object = MyClass()

print(my_object.non_existent_attribute) # AttributeError

# NotImplementedError --> Happens when we try to use a feature that is not implemented yet

def my_function():
    raise NotImplementedError("This function is not implemented yet")

my_function() # NotImplementedError


# RuntimeError --> Happens when we try to do something that is not possible

def my_function():
    raise RuntimeError("This function is not possible")


# SyntaxError --> Happens when we have a syntax error in our code

print("Hello World" # SyntaxError
      
           
# IndentationError --> Happens when we have an indentation error in our code

a = 10
if a>0:
print("Hello World")
print("Hello World")
else:
    print("Hello World") # IndentationError    

# TabError
# TypeError
# ValueError
# ImportError
# DeprecationWarning
