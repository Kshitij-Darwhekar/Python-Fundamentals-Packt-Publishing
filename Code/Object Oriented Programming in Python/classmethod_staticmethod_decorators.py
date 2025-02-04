# Classmethod and Staticmethod Decorators in Python
# classmethod and staticmethod are two types of decorators
# classmethod is used to create a class method
# staticmethod is used to create a static method

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        avg = sum(self.marks)/len(self.marks)
        return avg
    
rolf = Student('Rolf', 'School of Computing')
rolf.marks.append(90)
rolf.marks.append(85)
rolf.marks.append(95)
print(rolf.average())

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)
# classmethod has a cls argument
# Used when you need the access to a class



my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print('hi')

# Staticmethod has no self argument
# Used when you don't need access to a class but it is somehow related to the class


another_object = Bar()
another_object.hi()
