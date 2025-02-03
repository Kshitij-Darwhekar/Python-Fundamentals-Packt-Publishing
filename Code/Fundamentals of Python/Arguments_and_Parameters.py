# Arguments and Parameters in Python

car = {
    'color': 'blue',
    'make': 'Toyota',
    'model': 'Camry',
    'mileage': 100,
    'year': 2020,
    'fuel_consumed': 15
}

def calculate_mpg(car):
    mpg = car['mileage'] / car['fuel_consumed']
    print(f'The car does {mpg} miles per gallon')

calculate_mpg(car)

# Output:
# The car does 6.666666666666667 miles per gallon
