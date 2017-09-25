i = 1
while True:
    four = i * 4
    five = i * 5
    print('DEBUG i x*4 x*5', i, four, five)
    one = set(str(four))
    two = set(str(five))
    print('DEBUG made sets', one, two)

    if one == two:
        break

    i+=1