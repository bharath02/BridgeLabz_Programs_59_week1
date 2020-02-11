# filp Coin
import random

N= int(input("Enter a Coin: "))
result={"head":0,
        "tail":0,}
sides=list(result.keys())
for i in range(0,N):
    result[random.choice(sides)]+=1
    
print("Head probability is: ", result["head"])
print("Tail probability is: ", result["tail"])
