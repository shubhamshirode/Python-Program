def add():
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    c = a + b
    print('additon is', c)
def sub():
    a1 = int(input("enter the number"))
    b1 = int(input("enter the number"))
    c1 = a1 - b1
    print('Substraction is', c1)
def mult():
    a2 = int(input("enter the number"))
    b2 = int(input("enter the number"))
    c2 = a2 * b2
    print('multiplication is', c2)

while True :
    print("select the operation  1.addition  2.substraction  3.multiplication  4.exits")
    choice=int(input())
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice == 3:
        mult()
    elif choice == 4:
        break
    else :
        print("enter the number correctly")