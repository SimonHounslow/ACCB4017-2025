Line = int(input("Please enter line length: "))
count=0
while count<Line-1:
    print("x",end="",flush=True)
    count+=1

print("x")

print(f"a line of length {Line} has been displayed")