#A - string
def find_sequence(A):

    k = 1
    m = len(A)

    try:
        int(A)  # check if n - int - if yes - continue
        while True:
            s = ''  # where we will look for n
            for i in range(m):
                s += str(k + i)
            if A in s:
                # we found it, need to find index now
                h = s.find(A) + 1  # find n in last part of the sequence
                kn = ''
                for l in range(1, k):
                    kn += str(l)
                result = len(kn) + h
                break
            k += 1
    except Exception as e:
        result = 'You have typed the wrong sequence'
    finally:
        return result

answer = find_sequence('588')
print(answer)