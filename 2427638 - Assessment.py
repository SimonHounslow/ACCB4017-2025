while True:
    try:
        print("Please enter the values needed to calculate the volume of a pyramid:")
        SideA=float(input("Please enter the length of the base: "))
        Height=float(input("Please enter the height: "))
        if SideA>0 and Height>0:
            break
        else:
            print("Negative Values entered, try again")
    except Exception:
        print("Bad data entered, try again")

Volume=(SideA*SideA)*(Height/3)

print(f"The volume of the pyramid is: {round(Volume,2)}, rounded to 2 decimal places")