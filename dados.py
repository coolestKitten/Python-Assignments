#Coloca aquí tus funciones
def tirada(sq, t1,t2):
    sqtot = sq
    sq = t1 + t2
    if t1 == t2:
        sq = sq * 2
    sqtot = sqtot + sq 
    
    if sqtot % 5 == 0:
        sqtot = sqtot + 2
    return sqtot
  

#------[Sección de código no modificable]--------
tiradas = int(input())
avance = 0
for t in range(tiradas):
 d1 = int(input())
 d2 = int(input())
 avance = tirada(avance, d1,d2)
print(avance)
#------------------------------------------------