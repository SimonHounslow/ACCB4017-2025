import random
from ipaddress import collapse_addresses

Continue = "y"

while Continue =="y":
    number = random.randint(0,100)
    guess=-1
    counter = 0
    while guess !=number:
        guess = int(input("Please guess the number: "))
        counter+=1
        if guess>number+10 or guess<number-10:
            print("cold")
        else:
            if guess>number+4 or guess<number-4:
                print("warm")
            else:
                if guess!=number:
                    print("hot")
                else:
                    print(f"You took {counter} guesses")
    Continue=input("y to continue")