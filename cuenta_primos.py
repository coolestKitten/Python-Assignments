import random
primos = 0
while primos < 3:
    num = random.randint(0,10)
    cuenta = 0
    for div in range(1,num+1):
        if num%div==0:
            cuenta = cuenta + 1
    if cuenta==2:
        print(num,"es primo")
        primos = primos + 1
    else:
        print(num)
