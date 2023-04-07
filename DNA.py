strand = input()
strand = strand.upper()

div = len(strand)


print ('C',str((strand.count('C') / div) * 100) + '%')
print ('G',str((strand.count('G') / div) * 100) + '%')
print ('A',str((strand.count('A') / div) * 100) + '%')
print ('T',str((strand.count('T') / div) * 100) + '%')

