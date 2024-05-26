# Chek the number is prime or not.

n=int(input("enter the number"))
for x in range(1,n+1):
    if n%x==0:
        print(x,end=" ")
if x==2:
    print(n,"number is prime")
else:
    print(n,"number is not prime")
