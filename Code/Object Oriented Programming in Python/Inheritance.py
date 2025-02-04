# Inheritance in Python
# Inheritance is a mechanism in object oriented programming that allows one class to inherit the properties and methods of another class
# Inheritance is a way to reuse code and create a hierarchy of classes
# Inheritance is a way to create a new class that is based on an existing class

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        avg = sum(self.marks)/len(self.marks)
        return avg
    
        

# class WorkingStudent:
#     def __init__(self, name, school, salary):
#         self.name = name
#         self.school = school
#         self.salary = salary
    
#     def average(self):
#         avg = sum(self.marks)/len(self.marks)
#         return avg

# rolf = WorkingStudent('Rolf', 'School of Computing', 15.50)
# print(rolf.salary)


# In the above code, we created a new class called WorkingStudent 
# that is based on the Student class
# That is there is too man duplication

# That's where inheritnace comes in
# We can create a new class called WorkingStudent that is based on the Student class

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        # self.name = name
        # self.school = school
        super().__init__(name, school)
        self.salary = salary
    
    def weekly_salary(self):
        return self.salary * 52
    
    
    # def average(self):
    #     avg = sum(self.marks)/len(self.marks)
    #     return avg
    
    # we no longer need theis avg method since we are inheriting this method from Student
    
    
rolf = WorkingStudent('Rolf', 'School of Computing', 15.50)
print(rolf.salary)
rolf.marks.append(90)
rolf.marks.append(85)
rolf.marks.append(95)
print(rolf.average())
print(rolf.weekly_salary())


anna = Student('Anna', 'Oxford')
