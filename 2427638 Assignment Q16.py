age=[]
i=1
Rolling_Total=0

while i <7:
    while True:
        try:
            Age_Input = float(input(f"Enter age for person {i} in group:"))
            if Age_Input>0:
                i=i+1
                age.append(Age_Input)
                Rolling_Total=Rolling_Total+Age_Input
                break
            else:
                print("Bad age entered, try again")
        except Exception:
            print("Bad data try again")


print(age)

Average= Rolling_Total/6

print(f"The average is: {round(Average,2)}")
