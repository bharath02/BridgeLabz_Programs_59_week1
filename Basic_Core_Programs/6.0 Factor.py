import math
def factor(Number):
    while(Number%2==0):
        print(2)
        Number=Number/2
    for i in range(3,int(math.sqrt(Number))+1,2):
            while(Number%i==0):
                print(i)
                Number=Number/i
    if(Number>2):
        print(Number)
    
Number=int(input("Enter a Value: "))
factor(Number)
