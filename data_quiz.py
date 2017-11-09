with open('C:\\girl\\hey.txt') as f:
    strings = [s.rstrip() for s in f.readlines()]
otsenki = [s.split(';')[1:] for s in strings]
for x in otsenki:
    print(sum(map(int, x))/len(x))
sr_mat = sum([int(x[0]) for x in otsenki]) / len(otsenki)
sr_fiz = sum([int(x[1]) for x in otsenki]) / len(otsenki)
sr_rus = sum([int(x[2]) for x in otsenki]) / len(otsenki)
print(sr_mat, sr_fiz, sr_rus)
