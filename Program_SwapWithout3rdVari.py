#swap without using third Variable

x=int(input("enter the first number"))
y=int(input("enter the second number"))
x=y+x
y=x-y
x=x-y
print("x is",x,"y is",y)
