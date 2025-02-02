# Destructuring in Python
# Destructuring is a way to unpack the values from a sequence into variables
# It is a way to unpack the values from a sequence into variables

currencies = 0.8, 1.2
usd, eur = currencies
print(usd)
print(eur)
# Here the code will unpack the values from the tuple into the variables

friends = [('Rolf', 25), ('Anne', 37), ('Charlie', 31), ('Bob', 22)]
for friend, age in friends:
    print(f"{friend} is {age} years old.")
# Here the code will unpack the values from the tuple into
# the variables (Friend and age) and print the values

