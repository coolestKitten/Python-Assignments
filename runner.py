x = int(input())
array = []


while x != 0:
    num = int(input())
    array.append(num)
    
    x = x - 1
    

jump = 0
run = array.count(0)
l = len(array) - 1

for i, item in enumerate(array):
    if item == 0 and i + 1 <= l:
        if array[i - 1] == 1 and array[i + 1] == item:
            jump = jump + 1
        elif array[i - 1] == 1 and array[i + 1] == 1:
            jump = jump + 1
        elif array[i - 1] == 1 and i + 1 > l:
            jump = jump + 1
    elif item == 0 and i + 1 > l and array[i - 1] == 1:
        jump = jump + 1


if array.count(1) == len(array):
    jump = 1
   
            

print(run)
print(jump)
