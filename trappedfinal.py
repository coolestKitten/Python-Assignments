x = int(input())
array = []
trapped = []

while x != 0:
    num = int(input())
    array.append(num)
    
    x = x - 1
    
l = len(array) - 1

for i, item in enumerate(array):
    if i == 0:
        if item < array[i + 1]:
            trapped.append(item)
            
    elif i + 1 > l:
        if item < array[i - 1]:
            trapped.append(item)
                
    else:
        if item < array[i + 1] and item < array[i - 1]:
            trapped.append(item)


for i, item in enumerate(trapped):
    print(str(item))