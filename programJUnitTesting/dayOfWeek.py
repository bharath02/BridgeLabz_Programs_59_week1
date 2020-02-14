# day of week
import math
def Day_of_date(days,Month,year):
    yea=year-(14-Month)/12
    do=yea+int(yea/4)-int(yea/100)+int(yea/400)
    mo= Month+12*((14-Month)/12)-2
    dates=(days + do + (31*mo)/12)%7
    if(dates==0):
        print("Sunday")
    elif(dates==1):
        print("Monday")
    elif (dates == 2):
        print("Thuseday")
    elif (dates == 3):
        print("Wednesday")
    elif(dates==4):
        print("Thursday")
    elif(dates==5):
        print("Friday")
    elif(dates==6):
        print("Saturday")


days=int(input("enter a date of for finding a day 1 to 31 : "))
month=int(input("enter a date of for finding a month 1 to 12 : "))
year = int(input("Enter a year : "))
if((days>=1 and days<=31)or(month>=1 and month<=12) or(year>999)):
    Day_of_date(days,month,year)