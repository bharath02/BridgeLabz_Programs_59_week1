Number=int(input("Enter a Number"))
factor=2
while(Number!=0):
	if(Number%factor==0):
		print(factor)
                Number/=factor
	else:
             factor+=1
