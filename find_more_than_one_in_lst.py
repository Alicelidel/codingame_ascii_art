Numbers = input().split()
result = []
arr = [n for n in Numbers if Numbers.count(n)>1]
for i in arr:
    if i not in result:
        result.append(i)
for i in result:
    print(i, end=' ')