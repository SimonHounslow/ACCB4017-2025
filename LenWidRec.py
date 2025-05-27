Line = int(input("Please enter rectangle width: "))

RecLen = int(input("Enter height of rectangle: "))
Counter = RecLen
while Counter>0:
    count = 0
    while count < Line - 1:
        print("x", end="", flush=True)
        count += 1

    print("x")
    Counter-=1

print(f"A {Line}x{RecLen} rectangle has been drawn")