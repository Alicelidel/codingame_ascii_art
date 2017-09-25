matrix = []

while True:
    elem = input().split(' ')
    if elem[0] == 'end':
        break
    matrix.append(elem)
k = len(matrix)
m = len(matrix[0])

stroka = ''

for i in range(k):
    stroka = ''
    for j in range(m):
        # print(matrix[i][j])
        num = 0
        snum = ''
        if j == 0:
            num += int(matrix[i][m - 1])
        else:
            num += int(matrix[i][j - 1])

        if j == m - 1:
            num += int(matrix[i][0])
        else:
            num += int(matrix[i][j + 1])

        if i == 0:
            num += int(matrix[m - 1][j])
        else:
            num += int(matrix[i - 1][j])

        if i == k - 1:
            num += int(matrix[0][j])
        else:
            num += int(matrix[i + 1][j])

        stroka += str(num)
        if j < m - 1:
            stroka += ' '
    print(stroka)