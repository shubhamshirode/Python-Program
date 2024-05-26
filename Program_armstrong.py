# Chek weather the number is armstrong or not

num=int(input("enter the three digit number"))
a=num//100
n=num%100
b=n//10
c=n%10

sum=a**3+b**3+c**3
if sum==num :
    print("number is armstrong")
else:
    print("number is not armstrong")

