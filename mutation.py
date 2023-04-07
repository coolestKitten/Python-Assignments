strandDNA = input()
strandDNA = strandDNA.upper()

strandRNA = input()
strandRNA = strandRNA.upper()

baselist = []

iD = 0

err = 0

for x in strandRNA:
    baselist.append(x)

if len(strandDNA) < len(strandRNA):
    print('INSERCION')
elif len(strandDNA) > len(strandRNA):
    print('DELECION')
else:
    for n in strandDNA:
        if n == 'A' and baselist[iD] != 'U':
            err += 1
        elif n == 'G' and baselist[iD] != 'C':          
            err += 1
        elif n == 'T' and baselist[iD] != 'A':            
            err += 1
        elif n == 'C' and baselist[iD] != 'G':          
            err += 1
        else:
            iD += 1
            
    if err == 0:       
        print('NORMAL')
    else:
        print('SUSTITUCION')
            
            
        
    
           
        