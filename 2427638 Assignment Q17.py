def getnumber():
    while True:
        try:
            SideLength = float(input(f"Enter your measurement:"))
            if SideLength>0:
                break
            else:
                print("Bad length entered, try again")
        except Exception:
            print("Bad data try again")
    return SideLength

LengthMeasured = getnumber()
WidthMeasured = getnumber()
HeightMeasured = getnumber()

print(f"The measurements you entered (length/width/height) were: {LengthMeasured}  {WidthMeasured}  {HeightMeasured}")
print(f"The volume of the parcel is: {round(LengthMeasured*WidthMeasured*HeightMeasured,2)}")