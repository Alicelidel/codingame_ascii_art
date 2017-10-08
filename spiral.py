N = int(input())

matrix = [[[0] for i in range(N)] for i in range(N)]




k=1
r=0
d=N
while N>= 1:
    for j in range(r,d):
        matrix[r][j]=k
        k+=1
    for j in range(r+1,d):
        matrix[j][d-1]=k
        k+=1
    for j in range(d-2,r-1,-1):
        matrix[d-1][j]=k
        k+=1
    for j in range(d-2,r,-1):
        matrix[j][r]=k
        k+=1
    r=r+1
    d=d-1
    N-=2


for line in matrix:
    print(*line)