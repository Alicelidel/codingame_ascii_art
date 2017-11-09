with open('D:\\Загрузки\\dataset_3380_5.txt', 'r') as file:
    text = file.read()
    text = text.split('\n')
    print(len(text))

well = dict()
for i in range(1,12):
    well[str(i)] = 0

classs = []
names = []
heights = []


for st in text:

    try:
        print(st)
        klass, name, height = st.split('\t')
        classs.append(klass)
        names.append(name)
        heights.append(height)
    except:
        print(st)


for i in range(1,12):
    num = classs.count(str(i))
    #print(i, num)
    ttl = 0
    for k in range(len(classs)):
        if classs[k] == str(i):
            ttl += int(heights[k])
    ttl = ttl / num
    if ttl == 0:
        print(i, '-')
    else:
        print(i, ttl)