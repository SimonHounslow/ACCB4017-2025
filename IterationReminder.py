number_1 = int(input("Please enter first number: "))
number_2 = int(input("Please enter second number: "))

if number_1 > number_2:
    while number_1 >=number_2:
        print(number_1)
        number_1-=1
else:
    while number_1 <=number_2:
        print(number_1)
        number_1+=1
