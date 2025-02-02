# For Loop in Python
# For loops are used to iterate over a sequence (list, tuple, string, etc.)
# The code block will keep executing as long as the sequence has more items

friends = ['Rolf', 'Jen', 'Bob', 'Anne']

for friend in friends:
    print(friend)
# Here the code will run till the sequence has more items
# The code will print each item in the list

for index in range(4):
    print(friends[index])
# Here the code will run till the range has more items
# The code will print each item in the list

for index in range(2,5):
    print(index)

students = [
    {'name': 'Rolf', 'grade': 90},
    {'name': 'Bob', 'grade': 78},
    {'name': 'Jen', 'grade': 100},
    {'name': 'Anne', 'grade': 80},
]

for student in students:
    name = student['name']
    grade = student['grade']
    print(f"{name} has a grade of {grade}")
# Here the code will run till the sequence has more items
# The code will print each item in the list
