# Prime Number 0 to 1000

N=1000
for prime in range(2,N):
    count=0
    for j in range(2,prime//2):
        if(prime%j==0):
            count+=1
    if(count==0):
        print(prime, end=" " )
        
        
