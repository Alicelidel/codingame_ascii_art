diagonal = 1
for i in range(3,1170,2):
    print(i)
    diagonal += i**2 + (i**2) - (i-1)*1 + (i**2) - (i-1)*2 + (i**2) - (i-1)*3
    print(diagonal)