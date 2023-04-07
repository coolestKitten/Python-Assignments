c = int(input())

te = 0
el = 0
tw = 0

p = 0
t = 0

while c != 0:
    n = int(input())
    
    if n == 10:
        te = te + 1
    elif n == 11:
        el = el + 1
    elif n == 12:
        tw = tw + 1
    c = c - 1

if te == 2 or el == 2 or tw == 2:
    p = p + 1
print (p)

if te == 3 or el == 3 or tw == 3:
    t = t + 1
print (t)
    
    
    
    