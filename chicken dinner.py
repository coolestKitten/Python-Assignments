cartas=int(input())
x=0
dcartas=0
ocartas=0
docartas=0
cuentapar=0
cuentatercia=0
while x<cartas:
    a=int(input())
    x=x+1
    if a==10:
        dcartas=dcartas+1
    if a==11:
        ocartas=ocartas+1
    if a==12:
        docartas=docartas+1
    
if dcartas==2:
    cuentapar=cuentapar+1
if ocartas==2:
    cuentapar=cuentapar+1
if docartas==2:
    cuentapar=cuentapar+1
print(cuentapar)
if dcartas==3:
    cuentatercia=cuentatercia+1
if ocartas==3:
    cuentatercia=cuentatercia+1
if docartas==3:
    cuentatercia=cuentatercia+1
print(cuentatercia)