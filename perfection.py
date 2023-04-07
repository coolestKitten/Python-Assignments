n = int(input())

d = 1

s = 0

while d < n:
    if (n % d == 0):
        s = s + d
        d = d + 1
    else:
        d = d + 1

if s == n:
    print ('PERFECTO')
else:
    print ('NO PERFECTO')
    


