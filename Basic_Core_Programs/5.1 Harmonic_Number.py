def Harmonic_Number(N):
    
    if(N>0 and N==1):
        return 1
    return (1/N)+Harmonic_Number(N-1)
harmonic_number1=int(input("enter a range for Harmonic Number: "))
print(Harmonic_Number(harmonic_number1))
