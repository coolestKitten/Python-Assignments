x = int(input())
array = []


while x != 0:
    num = int(input())
    array.append(num)
    
    x = x - 1
    
l = len(array) - 1

for i, item in enumerate(array):
    if i == 0:
        print(item, i, 'this is the first number on the list', array[i+1])
    elif i + 1 > l:
        print(item, i, 'this is the end')
    else:
        print(item, i, 'this number is in the middle')

        
        
