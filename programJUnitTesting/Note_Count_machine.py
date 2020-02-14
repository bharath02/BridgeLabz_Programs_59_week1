#Find the Fewest Notes to be returned for Vending Machine, 1, 2, 5, 10, 50, 100, 500 and 1000
def Money(money):
    notes=[5000,2000,500,200,100,50,20,10,5,2,1]
    noteCounter=[0,0,0,0,0,0,0,0,0,0,0]
    print("Currency Counting    :- ")
    for i in (notes):
        for j in (noteCounter):
            if(money>=i):
                j=money//i
                money=money-j*i
                print(i,"   :  ",j)
                

money=int(input("Enter a Money of purchases"))
Money(money)