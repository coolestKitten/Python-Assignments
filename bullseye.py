import math

tx1 = float(input())
ty1 = float(input())
tx2 = float(input())
ty2 = float(input())

s = 0

cx = 0
cy = 0

d1 = math.sqrt(pow(cx - tx1,2) + pow(cy - ty1,2))
if d1 > 1 and d1 < 4:
    s = s + 80
elif d1 <= 1 and d1:
    s = s + 100
    
d2 = math.sqrt(pow(cx - tx2,2) + pow(cy - ty2,2))
if d2 > 1 and d2 < 4:
    s = s + 80
elif d2 <= 1 and d2:
    s = s + 100

print (s)