year1=int(input("Enter a Year: "))
def leapyear(year):
    if(year>999 and year<9999):
        if(year1%4==0):
            if(year1%100==0):
                if(year1%400==0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False
if(leapyear(year1)):
    print(year1,"Leap Year")
else:
    print(year1,"Not Leap Year")
