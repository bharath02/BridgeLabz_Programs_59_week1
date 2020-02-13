# Recursion of Permutation
print("Recursion of Permutation")
def to_String(char):
    
    return "".join(char)
def Permutation(char, start, end):
    if(start==end):
        print(to_String(char))
    else:
        for i in range(start,end+1):
            char[start],char[i]=char[i],char[start]
            Permutation(char,start+1, end)
            char[start],char[i]=char[i],char[start]
string="ABC"
end=len(string)
char=list(string)
Permutation(char, 0, end-1)
              
# Iteration of Permutation

char="ABC"
print("Iteration of Permutation")
for i in range(len(char)):
    for j in range(len(char)):
        for k in range(len(char)):
           if(char[i]!=char[j]!=char[k]):
               if(char[i]!=char[k]):
                  print(char[i]+char[j]+char[k])
