
x = int(input())
y = int(input())

#1 define que numero es mayor y cual es menor
a = max(x,y)
b = min(x,y)

#2 se cumple mientras b > 0
while b != 0:

    mcd = b 
    b = a % b 
    a = mcd
    
#3 obtiene el mcm
if mcd == 0:
    mcm = max(a,b)
else:
    mcm = (x * y) // mcd


print(mcm)