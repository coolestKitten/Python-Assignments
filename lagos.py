x = int(input())
y = int(input())

a = max(x,y)
b = min(x,y)

f = 720

while b:
    d = b
    b = a % b
    a = d
t = (x * y) // d

f = f + t


h = f // 60
if h > 24:
    h = h - 12
elif h == 24:
    h = 0

m = f % 60
if m == 0:
    m = str('00')
elif m < 10:
    m = ('0'+str(m))


print (str(h) +':'+ str(m))

    