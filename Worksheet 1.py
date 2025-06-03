#Car Model
#Car Year of Production
#Car Make
#Car Fuel type
#Car Engine Size

#initial input
Make = str(input("Please enter vehicle make: "))
Model = str(input("Please enter vehicle model: "))

#Loop until a valid year input

EarliestYear = 1900
LatestYear = 2025
#fixed variable for oldest and newest vehicles produced, could import time library to update

YearMadeValid = False
while YearMadeValid != True:
    try:
        YearMade = int(input("Please enter the year made: (YYYY) "))
        if YearMade>=EarliestYear and YearMade<=LatestYear:
            #if valid then set valid = true
            YearMadeValid = True
        else:
            print(f"Please enter the year, between {EarliestYear} and {LatestYear}. ", end="")
    except:
        print(f"Please enter the year, between {EarliestYear} and {LatestYear}. ", end="")


#Loop until valid fuel type entered'
FuelTypeValid = False
while FuelTypeValid != True:
    FuelType = input("Please state fuel type: ").lower()
    if FuelType == "diesel" or FuelType == "petrol" or FuelType == "electric" or FuelType == "hybrid":
        FuelTypeValid = True
    else:
        print("Input either: diesel, petrol, electric or hybrid. ", end="")


#Loop until valid engine size entered
MinSize=0.0
MaxSize=22.0
EngineSizeValid = False
while EngineSizeValid!=True:
    try:
        EngineSize = float(input ("Please enter engine size/power output(KW): "))
        #input value should be between 0.0 and 22.0
        if EngineSize>MinSize and EngineSize<MaxSize:
            EngineSizeValid = True
        else:
            print("Input a value between 0.0and 12.0. ", end="")
    except:
        print("Input a value between 0.0and 12.0. ", end="")



print(f"Make:{Make}\nModel:{Model}\nYear of Production: {YearMade}\nFuel Type: {FuelType}\nEngine size/Power output: {EngineSize}")






