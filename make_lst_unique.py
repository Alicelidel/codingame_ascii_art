lst = [int(i) for i in input().split()]

seen = set()
result = []
for x in lst:
    if x in seen:
        continue
    seen.add(x)
    result.append(x)
for elm in result:
    print(elm, end=' ')