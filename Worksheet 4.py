#Generate five random treasure locations in the range 1-50 and store them in a list.
import random

LocationList = []
FoundLocations = []

count=0
while count<5:
    while True:
        AddLocation= random.randint(1,50)
        if AddLocation in LocationList:
            continue
        else:
            count += 1
            break
    LocationList.append(AddLocation)
LocationList.sort()

print(f"Locations:{LocationList}")
#used for debugging, now have a list of 5 unique locations.

print("Welcome to Treasure Island")
print("There are 5 treasure chests hidden across the island (locations 1-50)")
while True:
    if len(FoundLocations) ==5 :
        print("All locations found. ", end="")
        break
    while True:
        try:
            user_guess = int(input("Where would you like to search? (-1 to exit)"))
            if user_guess <= 50 and  user_guess>=1:
                break
            elif user_guess == -1:
                break
            else:
                print("Invalid Location - Please enter a valid location")
        except Exception:
                print("Not integer - Please enter a valid location")

    #that ensures a valid search is entered
    if user_guess == -1:
        break

    smallest_distance = 100
    for Location in LocationList:
        if user_guess in FoundLocations:
            print("",end="") #just to put something inside the if statement
        else:
            if user_guess > Location:
                distance = user_guess - Location
                if distance < smallest_distance:
                    smallest_distance = distance
            if user_guess < Location:
                distance =  Location - user_guess
                if distance < smallest_distance:
                    smallest_distance = distance
            if user_guess == Location:
                smallest_distance = 0
                FoundLocations.append(user_guess)

    #print(f"Distance:{smallest_distance}")
    #we now have the smallest distance to the closet treasure.

    if smallest_distance == 0:
        print("💰 TREASURE FOUND! You've struck gold! 1000 coins!")
    elif smallest_distance <3:
        print("🔥 BURNING HOT! The treasure is practically beneath your feet!")
    elif smallest_distance <5:
        print("♨️ Very Hot! Your metal detector is beeping rapidly!")
    elif smallest_distance <8:
        print("🌡️ Hot! You can sense something valuable nearby!")
    elif smallest_distance <13:
        print("😊 Warm! You're on the right track!")
    elif smallest_distance <19:
        print("😐 Cool! You might want to try elsewhere!")
    elif smallest_distance <25:
        print("🥶 Cold! You're quite far from any treasure!")
    else:
        print("🧊 Freezing! You're nowhere near any treasure!")


print("Game over, thankyou for playing.")