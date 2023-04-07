wagonlist = []
cargolist = []

wcount = int(input())

while wcount:
    cap = int(input())
    wagonlist.append(cap)
    wcount = wcount - 1
    
    
ccount = int(input())

while ccount:
    amt = int(input())
    cargolist.append(amt)
    ccount = ccount - 1
    
wID = 0

for i, item in enumerate(cargolist):
    while item:   
        if item <= wagonlist[wID]:
            wagonlist[wID] = wagonlist[wID] - item
            item = 0
            wID = 0
           
        else:
            wID += 1
            if wID > len(wagonlist) - 1:
                item = 0
                wID = 0
        
print(wagonlist)