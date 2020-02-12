#Creating a Gambler game with tossing coins
import random
import numpy as np
random.random()
def Gambler():
    money,count=10,0
    while money:
        toss =  np.random.random()
        if toss <.50:
            money-=1
        if toss <.50:
            money+=1
        count+=1
    return count
sims=[Gambler() for i in range(500)]
print(len(sims))
np.mean(sims)
