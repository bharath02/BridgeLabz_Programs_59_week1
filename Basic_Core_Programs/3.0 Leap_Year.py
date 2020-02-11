# Leap Year
year=int(input("Enter a Year: "))
if(year>999 and year<9999):
    if(year%400==0 or(year%4==0 and year!=100)):
        print(year ,"is leap Year")
    else: 
        print(year,"Not Leap Year")
else: 
        print(year,"not a year and should be 4 digits")
