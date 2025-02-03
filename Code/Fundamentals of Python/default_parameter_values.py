# Default Parameter Values in Python
# Default parameter values are used to specify a default value for a parameter.
# If a parameter is not provided when the function is called, the default value will be used.

def add(x,y=3):
    total = x + y
    return total

print(add(5))

# Output:
# 8
# here y=3 is default value for y 

print(add(5,10))

#error
# print(add(x=5,2))

print(add(5,y=10)) # here y=10 is passed as an argument

print(1,2,3,4, sep=", ") # sep is a default parameter value

# When python defines a function it stores the defatult value
# in the function definition
# meaning if we set a default value to some variable and then change it 
# the default value will not change

num = 5

def add(x,y=num):
    total = x + y
    return total

print(f"When the value of y is {num} & x is 5 addition is: ",add(5))

# Output:
# 10

num=10
print(f"When the values of y is {num} & x is 5 addition is: ",add(5))

# Output:
# 10

# therefore it is highly discouraged to use variable as defaut values
