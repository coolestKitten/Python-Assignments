n = int(input())
e = 1
m = 0
et = 0

while n != 0:
    while e != 0:
        e = int(input())
        n = n - 1
        if e != 0:
            et = et + 1
    
    if et == 2:
        m = m + 10
    elif et == 3:
        m = m + 18
    elif et == 4:
        m = m + 37
    et = 0
    e = 1
        

print (m)
    
    
    