#input values
MyList = []

captured = int(input("Enter Value: "))

while captured !=-1:
    found = False
    #check if in list
    if len(MyList)>0:
        counter = 0
        while counter < len(MyList):
            if captured == MyList[counter]:
                found = True
                break
            counter+=1

    if found == False:
        # add if ok to add
        MyList.append(captured)

    captured=int(input("Enter Value: "))

#ouput list
print(MyList)