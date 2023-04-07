chain = ["R", "D", "M", "S", "STOP", "K", "M", "C", "W", "STOP"]
finalChain = []

startChain = False

for i, item in enumerate(chain):
    if (item == 'M'):
        startChain = True
    if (item == 'STOP'):
        startChain = False
        print(finalChain)
        finalChain.clear()
        
    if (startChain == True):
        finalChain.append(item)
    
    
    
