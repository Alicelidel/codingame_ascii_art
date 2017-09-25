list = []

for i in range(3,114):
    for j in range(3,106):
        x = i ** j
        print(x)
        if x not in list:
            list.append(x)

print(len(list))