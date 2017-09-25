counter = 0

for num in range(1, 12407):

    current_num = num

    for i in range(50):

        reversed_num = str(current_num)[::-1]

        summ = str(current_num + int(reversed_num))

        reversed_summ = summ[::-1]

        #print('comparing', summ, reversed_summ)

        if reversed_summ == summ and len(reversed_summ)>1:

            print(summ, i)

            break

        current_num = int(summ)
    else:
        counter+=1

print('count', counter)