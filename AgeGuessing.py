User1Age = int(input("Please enter age of first person: "))
User2Guess = int(input("Please enter your age guess: "))

if User1Age==User2Guess:
    print("Good Guess")
else:
    if User1Age<(User2Guess+5) and User1Age>(User2Guess-5):
        print("Warm")
    else:
        print("Cold")

print("All done")