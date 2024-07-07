age = 34

print(f"You are {age}")

# f string : IN F string you can type f and after in double qutations write your string, 
# you can add curly braces and your variable inside the curly braces


# In f string you cant chnage the variable

name = "Jose"
gretting = f"How are you {name} ?"

print(gretting)


name = "Bob"

print("after updating the name to bob")
print(gretting)


# Another way of formatting a string in Python

name = "jose"
final_greeting = "How are you {} ?"

jose_greeting = final_greeting.format(name)

print(jose_greeting)

bob_greeeting = final_greeting.format(name)

print(bob_greeeting)