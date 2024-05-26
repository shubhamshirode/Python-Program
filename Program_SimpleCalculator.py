a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
cn=int(input("enter your choice"))
if cn==1:
    print('Addition is',a+b)
elif cn==2:
    print("substraction is",a-b)
elif cn==3:
    print("multiplication is",a*b)
elif cn==4:
    if b==0:
        print('not div by 0')
    else:
        print("division is",a/b)
else:
    print("wrong choice")
