# List

l=["a","b","c","d"]

print(l)
print(l[0])
print(l[2:8])

#print(l[6]) IndexError: list index out of range

print(l[1])
print(l[0])
print(l[::-1]) #reverse string

if "c" in l:
    print("found")
else:
    print("not found")

for x in l:
    print(x)

i=0
while i<len(l):
    print(l[i])
    i=i+1

#insertion ( add the eliment in list )
l.append("e") # default it will store in last of list
print(l)

l.insert(2,"aa") # aa will store in 2
print(l)

#update
l[2]="ab"
print(l)

#delete
#del[2]

print(l[-1])

l.clear() # it will clear the list
print(l)






