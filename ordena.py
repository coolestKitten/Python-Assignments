a = int(input())
b = int(input())
c = int(input())


f = min(a,b,c)
t = max(a,b,c)

c1 = min(a,b)
c2 = min(b,c)

if c1 > c2:
    s = c1
elif c2 > c1:
    s = c2
elif c2 == c1:
    s = b 


print(f)
print(s)
print(t)
