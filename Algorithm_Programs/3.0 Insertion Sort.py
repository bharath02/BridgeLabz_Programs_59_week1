# Insertion Sort
string=["Bharath", "Akhila","Aishwarya","Harika","sravya","Anusha","Tejashiwini","vidya"]
for i in range(0,len(string)):
    key=string[i]
    j=i-1
    while j>=0 and key < string[j]:
        string[j+1]=string[j]
        j-=1
    string[j+1]=key
print(string)
