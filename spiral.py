N = 2
matrix = [[1,2],[4,3]]

for j in range(N - 1, -1, -1):
    for i in matrix:

        print(i[j], end=" ")

    print()