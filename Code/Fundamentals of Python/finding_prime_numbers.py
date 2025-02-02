# Finding prime numbers in Python
# Prime numbers are numbers that are only divisible by 1 and themselves

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number")
# Here the code will run till the range has more items
