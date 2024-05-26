# Chek string is palindron or not.

s=input("enter the string")
a=(s)
b=(s[::-1])
if a==b:
    print("string is palindron")
else:
    print("string is not palindron")
