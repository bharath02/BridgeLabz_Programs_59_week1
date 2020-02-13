string=["Bharath", "Akhila","Aishwarya","Harika","sravya","Anusha","Tejashiwini","vidya"]
key=str(input("Enter a Name: "))
for i in range(len(string)-1):
    for j in range(len(string)-i-1):
        if(string[j]>string[j+1]):
            string[j],string[j+1]=string[j+1],string[j]
print(string)
start=0
end=len(string)-1
while(start<=end):
    middle=start+((end-start)//2)
    if(key==string[middle]):
        print(key, "successfully Search")
        break
    elif(key>string[middle]):
        start=middle+1
    else:
        end=middle-1
else:
    print(key,"Not Successfull search")
