# Convert a number into single digit

num=int(input("enter the four digit number"))
a=num//1000
n=num%1000
b=n//100
n=n%100
c=n//10
d=n%10

print(a,b,c,d)
