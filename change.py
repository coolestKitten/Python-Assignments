print ('Introduzca monto a pagar')
t = int(input())
print ('Introduzca cantidad con la que se va a pagar')
p = int(input())

c = p - t

f = c//5
d = (c-(5*f))//2
o = (c-(5*f)-(2*d))


print ('Su cambio son',f,'monedas de 5,',d,"monedas de 2 y",o,"monedas de 1")

