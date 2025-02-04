# magic methods in python
# magic methods are methods that are automatically called by python
# when we use them
# for example __init__ is a magic method

class Student:
    def __init__(self, new_name, new_age, new_grades):
        self.name = new_name
        self.age = new_age
        self.grades = new_grades

movies = ['Matrix','Finding Nemo','The Matrix Reloaded']

print(movies.__class__)

hi = "hello"
print(hi.__class__)

# everything is an obect in python

# Everything we can do with list we can do with classes

print(len(movies))

class Garage:
    
    # Used to initialize the object
    def __init__(self):
        self.cars = []
    
    # Used to calculate the length of the object
    def __len__(self):
        return len(self.cars)
    
    # Used to index an item in the object
    def __getitem__(self, index):
        return self.cars[index]
    
    # Used to return a string representing the object
    def __repr__(self):
        return f'Garage with {len(self.cars)} cars'
    
    # Used to return string
    def __str__(self):
        return f'Garage with {len(self.cars)} cars'
    
    # Diference between __str__ and __repr__
    # __str__ is used to return a string representing the object (This targeted at user) (Creates a human-readable representation of the object)
    # __repr__ is used to return an unambiguous representation of the object, which is useful for debugging and development. 
    
ford = Garage()
ford.cars.append('Ford Focus')
ford.cars.append('Ford Fusion')

print(ford.cars)

print(len(ford[0])) # Garage.__getitem__(ford, 0)
# Python can't calculate this 
# after adding the __len__ method this works

for car in ford:
    print(car)

