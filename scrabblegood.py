letterpool = []
points = []
score = 0

c = int(input())

while c:
    letterpool.append(input())
    points.append(int(input()))
    c -= 1
template = input()
    
iD = 0

for i in template:
    if i in letterpool:
        score += points[letterpool.index(i)]
    iD += 1
print(score)   
    
    

