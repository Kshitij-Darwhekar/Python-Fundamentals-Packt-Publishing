# Classes and Objects in Python

class Student:
    def __init__(self, new_name, new_age, new_grades):
        self.name = new_name
        self.age = new_age
        self.grades = new_grades

    def average_grade(self): # this is not called a function it is called a method even though both are the same thing
        avg = sum(self.grades)/len(self.grades)
        return avg
    
    

my_students = {
    'name': 'John',
    'age': 20,
    'grades': [90, 85, 95]
}

print(Student(my_students['name'], my_students['age'], my_students['grades']))

# We can also create a new object of Student class

john = Student('John', 20, [90, 85, 95])
jane = Student('Jane', 22, [90, 85, 95])

print(john.name)
print(john.average_grade())
print(jane.name)
print(jane.average_grade())