userinpt = input()

inptlist = userinpt.split()


for i in inptlist:
    i = i.replace("-","")
    i = i.replace('+','')
    i = i.replace('(','')
    i = i.replace(')','')
    if i.isdigit():
        print (i)