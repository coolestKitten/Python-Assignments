suma=0
codigo=int(input())
codigo2=int(input())
suma2=0

while codigo!=0:
    digito=codigo%10
    suma=suma+digito
    codigo=codigo//10
    if suma>9 and codigo==0:
        codigo=suma
        suma=0
while codigo2!=0:
    digito2=codigo2%10
    suma2=suma2+digito2
    codigo2=codigo2//10
    if suma2>9 and codigo2==0:
        codigo2=suma2
        suma2=0
    
if suma%2==0 and suma2%2==0:
    print('COMPATIBLES')
else:
    print('NO COMPATIBLES')