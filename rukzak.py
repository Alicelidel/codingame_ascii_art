# put your python code here
n, W = [int(a) for a in input().split()] #num of things, what we have

things = []

for i in range(n):
    c,v = [int(a) for a in input().split()] #totalcost, totalvolume
    #print(n, W, s, v)
    t=c/v #price for kg
    things.append([t, c, v])
#print(things)
#sort list
things.sort(reverse=True)
total = float(0) #total cost

for t, c, v in things: #in order from the biggest price for kg
    if W == 0:
        break #if no start volume then null
    elif W >= v:
        W -= v #if thing's volume is lower that overall volume
        total += c
    else:
        total += W*t #else thing's folume is bigger than overall volume
        W = 0

print(total)