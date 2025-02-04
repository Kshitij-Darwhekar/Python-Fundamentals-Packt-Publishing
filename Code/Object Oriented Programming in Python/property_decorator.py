# Property Decorator in Python

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        avg = sum(self.marks)/len(self.marks)
        return avg

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    
    @property
    def weekly_salary(self):
        return self.salary * 52

rolf = WorkingStudent('Rolf', 'School of Computing', 15.50)
print(rolf.salary)

#print(rolf.weekly_salary) # AttributeError: type object 'WorkingStudent' has no attribute 'weekly_salary'

# we can do thins only when the fuction doesn't have any arguments

# Now after adding the property decorator
# we can access the weekly_salary property
print(rolf.weekly_salary)