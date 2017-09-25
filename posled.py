n = int (input())
l = []
for i in range(n+1):
    l += [i]*i
print(l)
print (*l[:n], end = ' ')