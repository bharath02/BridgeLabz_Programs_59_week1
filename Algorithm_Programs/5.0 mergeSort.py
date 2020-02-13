# Merg Sort
def mergeSort(string):
    if(len(string)>1):
        mid = len(string)//2
        left=string[:mid]
        right=string[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while(i<len(left) and j < len(right)):
              if(left[i]<right[j]):
                  string[k]=left[i]
                  i+=1
              else:
                   string[k]=right[j]
                   j+=1
              k+=1
        while( i< len(left)):
            string[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            string[k]=right[j]
            j+=1
            k+=1
def printList(string):
    for i in range(len(string)):
        print(string[i],end=", ")
    print()
        
string=["Nagaraj","Dilip","Kranthi", "Prashanth","Jeevan","Bharath","SaiKumar","Sandeep","Naresh","Suvam"]
mergeSort(string)
printList(string)
