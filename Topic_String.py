# String
s="PHN technology"
l=len(s)
print(l)

u=s.upper()
print(u)

lo=s.lower()
print(lo)

t=s.title()
print(t)

c=s.capitalize()
print(c)

print(s.startswith("P"))
print(s.startswith("t"))

print(s.endswith("p"))
print(s.endswith("y"))

rep=s.replace("PHN","ABCdef")
print(rep)

sp=s.split()
print(sp)

print(sp[1])

print(sp[0])

print(s[::-1]) #reverse string

if "tech" in s:
    print("found")
else:
    print("not found")

for x in s:
    print(x)

print(s)

print(s[0])

print(s[2:5])
