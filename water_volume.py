import copy
# island is a list of lists
#  island = [
#      [2, 2, 2],
#      [2, 1, 2],
#      [2, 1, 2],
#      [2, 1, 2]
#  ]
def get_water_volume(island):
    #let's find MxN size of the island
    m = len(island)
    n = len(island[0])
    result = 0
    k = 1001
    # k - the lowest border of the island
    for i in [0,m-1]:
        for j in range(1,n-1):
            if k > island[i][j]:
                k = island[i][j]
    for i in range(1,m-1):
        for j in [0,n-1]:
            if k > island[i][j]:
                k = island[i][j]

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            elem = island[i][j]
            minum = min(island[i-1][j], island[i+1][j],
                        island[i][j-1], island[i][j+1])
            if elem < k:
                if elem < minum:
                    result += minum - elem
                    island[i][j] = minum
                elif elem < k:
                    result += k - elem
                    island[i][j] = k

    return result

island = [
    [56, 38, 40, 54],
    [157, 2, 1, 43],
    [38, 40, 1, 34],
    [87, 51, 44, 3]]

#print(len(island))
#print(len(island[0]))

hey = get_water_volume(island)

print(hey)