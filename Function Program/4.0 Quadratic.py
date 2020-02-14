# The Quadratic Function a*X*X+b*X+C
import math
def Quadratic(a, b, c,delta):

    X1=-b+int(delta)/2*a
    X2=-b-int(delta)/2*a
    print(a*X1*X1+b*X1+c, a*X2*X2+b*X2+c)

a=int(input("Enter a Value of a : "))
b=int(input("Enter a Value of b : "))
c=int(input("Enter a Value of c : "))
delta=math.sqrt((b*b)-(4*a*c))/2*a
Quadratic(a,b,c,delta)