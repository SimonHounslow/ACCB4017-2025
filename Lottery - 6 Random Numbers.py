#generate 6 random no repeating numbers
#sort in order
import random

while True:
    try:
        NumberDraws = int(input("Please enter the number of results to be drawn:"))
        break
    except ValueError:
        print(f"Error{ValueError}")

while True:
    try:
        MinNumber = int(input("Please enter the smallest possible number that can be drawn:"))
        break
    except ValueError:
        print(f"Error{ValueError}")

while True:
    try:
        MaxNumber = int(input("Please enter the largest possible number that can be drawn:"))
        if MaxNumber<MinNumber+NumberDraws-1:
            print (f"Max needs to be at least: {MinNumber+NumberDraws-1}")
        else:
            break
    except ValueError:
        print(f"Error{ValueError}")

NumberList = []
count=0
while count<NumberDraws:
    while True:
        AddNumber= random.randint(MinNumber,MaxNumber)
        if AddNumber in NumberList:
            continue
        else:
            count += 1
            break
    NumberList.append(AddNumber)

print(f"List: {NumberList}")

NumberList.sort()
print(f"Sorted: {NumberList}")