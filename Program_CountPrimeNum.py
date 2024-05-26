#count all the prime number between 1 to 50
n=1
pcnt=0
while n<=50:
    
    cnt=0
    for x in range(1,51):
        if n%x==0:
            cnt+=1
            
    if cnt==2:
        pcnt+=1
        
   # else:
        #print("not prime")
    n+=1
print(pcnt)
        
