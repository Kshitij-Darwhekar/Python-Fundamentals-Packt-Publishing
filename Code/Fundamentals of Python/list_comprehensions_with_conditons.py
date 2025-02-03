# List Comprehensions with Conditionals in

numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
guests = ["jose", "bob", "charlie", "david", "eve"]

friends_lower = [friend.lower() for friend in friends]

present_friends =[
    name.title() 
    for name in guests 
    if name.lower() in friends_lower
]

present_friends_string = ", ".join(present_friends)
print(f"Friends present in the party are {present_friends_string}")

# You should never nest list comprehension one inside another.
# This will make the code unreadable
