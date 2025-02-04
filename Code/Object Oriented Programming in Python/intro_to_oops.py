# Introduction to Object Oriented Programming

my_students = {
    'name': 'John',
    'age': 20,
    'grades': [90, 85, 95]
}

def average_grade(student):
    avg = sum(my_students['grades'])/len(my_students['grades'])
    return avg

print(average_grade(my_students))

# Bu there is a flaw in this code.
# The flaw is not in code itself but its design
# In a large project, my_students and the function average_grade could be in different files
# they are tightly coupled together


# We can solve this with objects

class Student:
    def __init__(self, new_name, new_age, new_grades):
        self.name = new_name # Self is a blank object and by Self.name we are creating a new variable called name in self object and giving them the value of new_name
        self.age = new_age # Similarly, we are crearing a new varibale are and passing th value of new_age
        self.grades = new_grades # Again, we are creating a new variable and passing the value of new_grades
    
    # Speical function __init__ is called when an object is created
    # It is used to initialize the object
    
    def average_grade(self):
        avg = sum(self.grades)/len(self.grades)
        return avg

# Now, let's create an object of Student class


student_two = Student('John', 20, [90, 85, 95])
student_three = Student('Jane', 22, [90, 85, 95])
print(student_two.name)
print(student_two.average_grade())
print(student_three.name)
print(student_three.average_grade())

