#find the prime numbers that are Anagram and Palindrome
N=1000
prime_number=[]
for prime in range(2,N):
    count=0
    for j in range(2,prime//2):
        if(prime%j==0):
            count+=1
    if(count==0):
        
        prime_number.append(prime)
print("Palindrome_Number  : ")       
for pali in range(len(prime_number)):
    key=prime_number[pali]
    if(prime_number[pali]>9):
        temp=0
        while(prime_number[pali]!=0):
            number=prime_number[pali]%10
            temp=(temp*10)+number
            prime_number[pali]=prime_number[pali]//10
            
        if(temp==key):
            print(temp, end=" ")
def updateFreq(n, freq):
    while(prime_number):
        digit=prime_number%10
        freq[digit]+=1
        prime_number//=10
def Anagram(a,b):
    freqA=[0]*10
    freqB=[0]*10
    updateFreq(a,freqA)
    updateFreq(b,freqB)
    for i in range(10):
        if(freqA[i]!=freqB[i]):
            return False
    return True
for i in range(len(prime_number)):
    for j in range(i+1,len(prime_number)):
        print(Anagram(prime_number[i],prime_number[j]))

        
