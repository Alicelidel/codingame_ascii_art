num = int(input())
i = 1
res = []

while True:
    if num - i <= i:
        res.append(num)
        break
    else:
        res.append(i)
        num -= i
        i += 1
print(len(res))
print(*res)