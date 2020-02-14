def loopStament(Number):
    for i in range(3):
        for j in range(3):
             print(Number,end=" ")
        print()

Number=input("enter a Number")
loopStament(int(Number))
loopStament(float(Number))
loopStament(bool(Number))
