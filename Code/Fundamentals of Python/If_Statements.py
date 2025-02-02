# If Statements in Python
# If are used to make decisions in Python based on cosme condition
# If the condition is true, the code block following the if statement is executed

friend = 'Rolf'
user_name = input('Enter your name: ')

if user_name == friend:
    print('Hello, friend!')
    print('I am Rolf')
    print('Nice to meet you')
else:
    print('Hello, stranger!')
    print(f"Nice to meet you, {user_name}")
    print("What brings you here?")

# bool Function
# It is used to convert a value to a boolean value

print(bool(5)) # True

# elif Statement
# It is used to add more conditions to the if statement

friends = ['Rolf', 'Bob', 'Jen']
family = ['Jen', 'Bob', 'Rolf']

user_name = input('Enter your name: ')

if user_name in friends:
    print('Hello, friend!')
    print('I am Rolf')
    print('Nice to meet you')
elif user_name in family:
    print('Hello, family!')
    print('I am Rolf')
    print('Nice to meet you')
else:
    print('Hello, stranger!')
    print(f"Nice to meet you, {user_name}")
    print("What brings you here?")
