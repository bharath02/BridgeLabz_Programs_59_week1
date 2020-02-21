# Write a Util Static Function to calculate monthlyPayment that reads in three command-line arguments P, Y, and R and calculates the monthly payments you would have to make over Y years to pay off a P principal loan amount at R per cent interest compounded monthly. The formula is The formula is
monthlyPay=20
Rate=30
years=2
n=12*years
r=Rate/(12*100)
print("Payment : ", (monthlyPay*r)/(1-(1+r)**(-n)),"%")