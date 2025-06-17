#Vehicle type select: Car/Motorcycle/Van/Bus
while True:
    vehicle_type = input("Please enter vehicle type: (Car, Motorcycle, Van, Bus)").lower()
    if vehicle_type == "car":
        break
    if vehicle_type == "motorcycle":
        break
    if vehicle_type == "van":
        break
    if vehicle_type == "bus":
        break
#while loop to validate vehicle selection


#Duration Hours
stay_duration = 0
while True:
    try:
        correct_duration = "y"
        stay_duration = float(input("Please enter the duration of stay in hours (0.5 is half hour)"))
        if stay_duration > 0:
            if stay_duration<1 or stay_duration>72:
                # Confirmation if larger than 72 or less than 1
                while True:
                    correct_duration = input(f"Is the duration correct: {stay_duration} (y/n)").lower()
                    if correct_duration == "n" or correct_duration == "y":
                        break
                #while to validate y/n on confirmation of duration
            if correct_duration=="y":
                #got stay duration longer than 0 hours and confirmed if above 72 or below 1
                break
    except Exception as e:
        print(f"Error on duration input{e}")
#while loop to validate stay duration


#max rate (per day, multiplies if larger than 24 hours)
# Car £15
# Motorcycle £6
# Van £25.00
# Bus £50.00

if stay_duration >24:
    number_of_days = int(round(stay_duration/24))
else:
    number_of_days = 1
max_cost = 0
if vehicle_type == "car":
    max_cost = number_of_days * 15
if vehicle_type == "motorcycle":
    max_cost = number_of_days * 6
if vehicle_type == "van":
    max_cost = number_of_days * 25
if vehicle_type == "bus":
    max_cost = number_of_days * 50

#duration captured with max possible fees depending on vehicle type and number of days stayed



while True:
    stay_weekend = input(f"Is the stay during the weekend? (y/n)").lower()
    if stay_weekend == "n" or stay_weekend == "y":
        break

#now know if it was on weekend or not to choose hourly rate for each type

cost=0 #initialise variable'

if vehicle_type == "car":
    cost = stay_duration * 2.5
    # Car £2.50
if vehicle_type == "motorcycle":
    cost = stay_duration * 1
    # Motorcycle £1.00
if vehicle_type == "van":
    cost = stay_duration * 4
    # Van £4.00
if vehicle_type == "bus":
    cost = stay_duration * 10
    # Bus £10.00

if stay_weekend == "y":
#multiply cost * 1.2 to increase by 20%
    cost = cost * 1.2

if cost>max_cost:
    cost = max_cost
#limit on the cost being charged

print(f"You stayed {stay_duration} at a cost of £{round(cost,2)}")




