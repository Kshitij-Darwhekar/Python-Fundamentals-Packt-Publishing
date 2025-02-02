# Break and Continue Statements in Python
# The break statement is used to exit the loop
# The continue statement is used to skip the current block and return to the for loop

cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']

for car_status in cars:
    if car_status == 'faulty':
        print('Stopping the production line!')
        break
    print(f'This car is {car_status}')  
# Here the code will run till the sequence has more items
# The code will print each item in the list
# The code will break the loop when the faulty car is found
