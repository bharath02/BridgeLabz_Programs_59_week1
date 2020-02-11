# filp Coin
import random

N= int(input("Enter a Coin: "))
count=0
for i in range(0,N):
    a=random.randint(0,1)
    if(a==0):
       count+=1
print("Head probability is: ", (count/N)*100)
print("Tail probability is: ", ((N-count)/N)*100)