def sum_integer_zero(lis,n):
    print("Sum of Triple Number is equal to zero :  ")
    for i in range(n-1):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(lis[i]+lis[j]+lis[k]==0):
                    print(lis[i],lis[j],lis[k])
lis=[0,-1,2,-3,1,4,-5]
n=len(lis)
sum_integer_zero(lis,n)