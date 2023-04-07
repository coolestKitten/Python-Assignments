votelist = []
votecount = []
candlist = []

#checks if there is a tie
def tiecheck(votecount):
     return all(x == votecount[0] for x in votecount)
    
#checks who the winner is
def winner(votelist):
    c = 0
    num = votelist[0]
   
    for i, item in enumerate(votelist):
        freq = votelist.count(item)
        if freq > c:
            c = freq
            num = item
    return num
        
#collects votes
n = int(input())

while n:
    vote = input()
    votelist.append(vote)
    if vote not in list(candlist):
        candlist.append(vote)
    n = n - 1
    
vID = 0

#prints each candidate along with its votecount
for x in range(len(candlist)):
     tally = votelist.count(candlist[vID])
     votecount.append(tally)
     name = candlist[vID]
     print (name, tally)
     vID += 1


#announces the winner or a tie if applicable
if tiecheck(votecount):    
    print('EMPATE')
else:
    
    print('GANA', winner(votelist))
