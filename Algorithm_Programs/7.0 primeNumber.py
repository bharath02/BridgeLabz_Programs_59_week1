# Prime Number 0 to 1000

N=1000
for i in range(2,N):
    count=0
    for j in range(2,i//2):
        if(i%j==0):
            count+=1
    if(count==0):
        print(i,end=" ",sep=" ")
        
