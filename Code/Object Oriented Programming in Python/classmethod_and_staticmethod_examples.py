# Examples of Classmethod and Staticmethod in Python

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f'FixedFloat({self.amount})'

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)
    
    
    
new_number = FixedFloat.from_sum(10, 20)
print(new_number)
# print(number)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'
        
    def __repr__(self):
        return f'{self.symbol}{self.amount}'
    

money = Euro(10)
print(money)

# now if we call the from_sum method using money it will work
# Since it has inherited the from_sum method from FixedFloat

money = Euro.from_sum(10, 20)
print(money)

# We will get the sum in FixedFloat object but we don't want that
# We want to get the sum in Euro object
# So we define the for_sum method as classmethod

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f'FixedFloat({self.amount})'

    @classmethod
    def from_sum(cls,value1, value2):
        return cls(value1 + value2)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'
        
    def __repr__(self):
        return f'{self.symbol}{self.amount}'

# Now when we call the from_sum method using Euro it will work
euro = Euro.from_sum(10, 20)
print(euro)

# here python is amart enough to include euro as the first argument i.e. cls