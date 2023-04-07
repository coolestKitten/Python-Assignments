#Coloca aquí tus funciones

def calcular_subtotal(valTy, valQt):
    if valTy == 1:
        sub = 700.0 * valQt
    else:
        sub = 900.0 * valQt
    return sub 

def calcular_descuento(valCs, valSb):
    if valCs == 1 and valSb >= 10000:
        desc = sub * 0.1
    elif valCs == 2:
        desc = sub * 0.2
    else:
        desc = 0.0
    return desc
def calcular_total(valSb, valDs):
    total = valSb - valDs
    
    return total
    
#----[No puedes modificar esta sección]----------
tipo = int(input())
cliente = int(input())
cant = int(input())

sub = calcular_subtotal(tipo, cant)
desc = calcular_descuento(cliente, sub)
total = calcular_total(sub, desc)
print(sub)
print(desc)
print(total)
#------------------------------------------------
