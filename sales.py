sales = []
bim = ['ENE-FEB','MAR-ABR','MAY-JUN','JUL-AGO','SEP-OCT','NOV-DIC']
c = 6
avg = 0

while c:
    
    sales.append(int(input()))
    c -= 1
    

iD = 0 

for i in sales:
     print(bim[iD],'|','#'*sales[iD], sales[iD])
     avg += sales[iD]
     iD += 1

print('PROMEDIO:',avg / 6)

