w = int(input())

print ("-"*w)
print ("-"*w)


c = int ((w-2)/2)
s = int(w % 2)

if s == 0:
    print (' '*(c-1),'||')
if s != 0:
    print (" "*(c-1),"|","|")
print ("-"*w)
print ("-"*w)

#print ("un"*c)