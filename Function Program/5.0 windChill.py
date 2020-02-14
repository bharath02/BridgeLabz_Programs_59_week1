#: the formula is not valid if t is larger than 50 in absolute value or if v is larger than 120 or less than 3 (you may assume that the values you get are in that range).
def windChill(tempe, speed):
    return (35.74+0.6215*tempe+(0.4275*tempe-35.75)*speed**0.16)
tempe=int(input("enter temperature is greater then 50 : "))
speed=int(input(("Enter a speed much be greater then 120 or less than 3 : ")))
if(tempe>50 and (speed>120 or speed<3)):
    print(windChill(tempe,speed))
else:
    print("PLease follow instructions while entering Temperature and speed ")