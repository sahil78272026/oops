# Not using oops is called procedural oriented programming

from ast import Num


class Number:  # PascalCase
    company = "google" # Class Variable
    def sumNum(self):  # camelCase
        return self.a + self.b
    

num = Number() # object Instantiation
num.a = 10  #  Instance variable , belongs to object
num.b = 20  #  Instance variable , belongs to object
print(num.sumNum()) # Number.sumnum(num)


# a = 12
# b = 34

# print("The sum of a and b is ", a+b)

'''
PascalCase 
EmployeeName -->PascalCase 

camelCase
isNumeric, isFloatOrInt -->camelCase
'''