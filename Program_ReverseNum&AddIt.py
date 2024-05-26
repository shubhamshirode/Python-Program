num=int(input("enter the four digit number"))
a=num%10
n=num//10
b=n%10
n=n//10
c=n%10
d=n//10

print(a,b,c,d)
f=(a*1000+b*100+c*10+d)
g=f + num
print("addition is ", g)
