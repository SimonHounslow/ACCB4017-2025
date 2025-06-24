print("What sort of food")
print("1. Normal")
print("2. Superfood")
while True:
    try:
        FoodType = int(input("Enter your choice (1 or 2):"))
        if FoodType ==1 or FoodType==2:
            break
    except ValueError:
        print("Input Error, try again")
print("")
while True:
    try:
        NoDays= int(input("How many days has your chicken been laying?"))
        if NoDays>0 and NoDays<180:
            break
        else:
            print("a number greater than 0 and less than 180 is required")
    except ValueError:
        print("Input Error, try again")
NoCakes= 0
DaysLeft=NoDays
if FoodType == 1:
    #normal food
    NoEggs = NoDays
    while DaysLeft>1:
        NoCakes+=1
        DaysLeft-=2
else:
    #superfood
    NoEggs=0
    while DaysLeft>1:
        DaysLeft-=2
        NoEggs+=3
    if DaysLeft == 1:
        NoEggs+=1
    NoCakes =int(NoEggs/2)
print(f"{NoDays} days that's {NoEggs} eggs and {NoCakes} cakes")