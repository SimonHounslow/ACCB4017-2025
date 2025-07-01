def addnumbers(Val1, Val2):
    return Val1+Val2

def subnumbers(Val1, Val2):
    return Val1-Val2

def multinumbers(Val1, Val2):
    return Val1*Val2

def divnumbers(Val1, Val2):
    return round(Val1/Val2,0)

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

print(addnumbers(num1,num2))
print(subnumbers(num1,num2))
print(multinumbers(num1,num2))
print(divnumbers(num1,num2))