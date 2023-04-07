n = int(input())
votelist = []
candlist = []

while n:
    vote = input()
    votelist.append(vote)
    if vote not in list(candlist):
        candlist.append(vote)
    n = n - 1
        
d = len(candlist)
ID = 0
votecount = []

#prints the winner with their respective tally

for i in range (d):
    c = votelist.count(candlist[ID])
    votecount.append(c)
    h = candlist[ID]
    print (h,c)
    ID += 1
    

#defines who wins and prints

j = (max(set(votelist), key=votelist.count))

if votecount.count(max(votecount)) > 1:
    print ('EMPATE')
else: 
    print('GANA', j)