XperRow = int(input("Please enter rectangle width: "))
#length of each line (so number of times to print "x")
XRows = int(input("Enter height of rectangle: "))
#hight of rectangle (so number of lines)
Counter = 0
#counter is now equal to the number of lines
while Counter<XRows:
    #do the below when Counter is greater than 0
    count = 0
    #this resets the number of x on each line
    while count < XperRow:
        print("x", end="",flush=True)
        count += 1
    print("")
    #normal print to finish line and move on
    Counter+=1
    #counter states how many rows have been printed
print(f"A {XperRow}x{XRows} rectangle has been drawn")