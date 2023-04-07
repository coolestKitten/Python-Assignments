# Casos
# a=10  b=20    10 12 14 16 18 20
# a=7   b=12    8 10 12
# a=3   b=5     4
a = int(input("a:"))
b = int(input("b:"))

#Solucion 2
if a%2==1:
    a = a + 1
while a<=b:
    print(a)
    a = a + 2    

#Solucion 1
#while a<=b:
#    if a%2 == 0:    
#        print(a)
#    a = a + 1
