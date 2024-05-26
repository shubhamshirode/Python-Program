fr={"apple":"20kg","banana":"25dz"}


print("1.add new fruit")
print("2.view all fruits")
print("3.sell a fruit")
print("4.notification")
print("5.update quantity")       
print("6.delete a fruit")
print("7.exit")
               

while True :
    ch=int(input("enter your choice : "))

    if ch==1:
     # print("add new fruit")
        
        f=input("enter the new fruit : ")
        g=input("enter the value : ")
        fr[f]=g
        #print(fr)
        
    elif ch==2:
       # print("view all fruits")
        print(fr)
        
    elif ch==3:
       # print("sell a fruit")
        c=input("enter fruit name  : ")
        if c in fr:
            print("availabe ")
            nq=input("enter the new value")
          #  nq=fr[c]
            print(nq)   
        else:
            print("fruit is not their : ")
            
    elif ch==4:
        #print("notification")
        print(fr) 

        
         
    elif ch==5:
       # print("update quantity")
       d=input("enter the update fruit : ")
       e=input("enter the update value")
       fr[d]=e
       print(fr)
        
    elif ch==6:
       # print("delete a fruit")
       f=input("enter the delete fruit name")
       del fr[f]
       print(fr)
        
    elif ch==7:
       # print("exit")
        print("exit...")
        break


else :
    print("wrong choice")

