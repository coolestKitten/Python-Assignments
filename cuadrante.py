deg = int(input())

if (deg == 0 or deg == 90 or deg == 180 or deg == 270 or deg == 360):
    print ('EJE')
elif 0 < deg < 90:
    print (1)
elif 90 < deg < 180:
    print (2)
elif 180 < deg < 270:
    print (3)
elif 270 < deg < 360:
    print (4)
else:
    print('EXCEDE')