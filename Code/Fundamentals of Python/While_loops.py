# While Loop in Python
# While loops are used to repeat a block of code multiple times
# The code block will keep executing as long as the condition is true

is_learning = True

while is_learning:
    print('You are learning!')
    user_input = input('Are you still learning? ')
    is_learning = user_input == 'yes'

print('We are done learning!')

# Here the code will run till the user_input is 'yes'
# If the user_input is 'no' the code will stop running

# Break Statement
# The break statement is used to break out of a loop
# It is used to stop the execution of the loop even if the condition is true

is_learning = True

while is_learning:
    print('You are learning!')
    user_input = input('Are you still learning? ')
    if user_input == 'no':
        break

print('We are done learning!')