import random
Coupon_Number=int(input("enter a Coupon Numbers : "))
Coupon_Value = random.sample(range(0,Coupon_Number),Coupon_Number)
for i in (Coupon_Value):
    print(Coupon_Value[i])
