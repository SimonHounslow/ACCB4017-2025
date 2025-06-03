import random

tosses = int(input("How many coin tosses? "))
headscounter =0
tailscounter =0

while tosses>0 :
    number=random.randint(0,1)
    if number==1:
        headscounter+=1
        print("Heads")
    else:
        tailscounter += 1
        print("Tails")
    tosses -=1

print(f"Total Heads : {headscounter}")
print(f"Total Tails : {tailscounter}")