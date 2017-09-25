for s in range(1,10):
    for y in range(1,10):
        for x in range(10):
            for u in range(10):
                for r in range(1,10):
                    syx = int(str(s) + str(y) + str(x))
                    yur = int(str(y) + str(u) + str(r))
                    rrsy = int(str(r) + str(r) + str(s) + str(y))
                    if syx+yur == rrsy:
                        print(syx, yur, rrsy)