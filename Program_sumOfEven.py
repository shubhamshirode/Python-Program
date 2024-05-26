#calculate sum of all the even factor of a given number n


n=int(input("enter the number"))
sum=0
for x in range (1,n+1):
    if n%x==0 and  n%2==0:
        sum+=x
    
print(sum)
    
