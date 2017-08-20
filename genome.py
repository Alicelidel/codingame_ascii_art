genome = input()+' '
s = 0
n=genome[0]
for i in genome:
    if n!=i:
        print(n + str(s), end = '\t')
        s=0
        n=i
    s+=1