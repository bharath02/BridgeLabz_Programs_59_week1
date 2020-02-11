N= int(input("Enter a Number: "))
if(N>=0 and N<31):
    for i in range(N):
        print("2 Power of ",i,"=", 2**i)
else:
    print(N,"Value Should lies Between 0 to 30")
