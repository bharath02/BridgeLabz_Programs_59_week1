#Bubble Sort
sort=["Nagaraj","Dilip", "Kranthi", "Prashanth","Jeevan","Bharath","SaiKumar","Sandeep","Naresh","Suvam"]
for i in range(0,len(sort)-1):
    for j in range(0,len(sort)-i-1):
        if(sort[j]>sort[j+1]):
            sort[j],sort[j+1]=sort[j+1],sort[j]
print(sort)
