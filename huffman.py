s = 'abacabadgggdjjssbbbbdhdhooirehfjhjfjfdbhvbhsvf' #input str to encode

def huffman(s):
    all = dict()
    codes = dict()
    res = ''
    for letter in s:
        if letter not in all:
            all[letter] = 0
        else:
            all[letter]+= 1

    #print(all.items())

    all_new = sorted(all.items(), key=lambda x: x[1], reverse=True)

    #print(all_new)

    c = len(all_new)
    e = len(all_new)
    #print(c)

    while c > 0:
        if c == 1:
            codes[s[0]] = '0'
        elif c == 2:
            letter, v = all_new.pop()
            codes[letter] = '10'
            c-=1
            letter, v = all_new.pop()
            codes[letter] = '0'
            c-=1
        else:
            if c == e:
                letter, v = all_new.pop()
                codes[letter] = '1' * (c - 1)
                c -= 1
            else:
                letter, v = all_new.pop()
                codes[letter] = '1' * (c - 1) + '0'
                c-=1
            #print(all_new)

    #print(codes)

    for letter in s:
        res += codes[letter]
    #print(codes)
    print(len(codes), len(res))
    for k, v in codes.items():
        #print(kv)
        print('{}: {}'.format(k, v))
    print(res)




huffman(s)
"""input is upwards
output:
total num of letters: 14 weight of a str: 231
letters:
e: 1111111111111
r: 1111111111110
i: 111111111110
c: 11111111110
v: 1111111110
o: 111111110
s: 11111110
g: 1111110
f: 111110
a: 11110
j: 1110
d: 110
h: 10
b: 0
encoded str:
111100111101111111111011110011110110111111011111101111110110111011101111111011111110000011010110101111111101111111101111111111101111111111110111111111111110111110111010111011111011101111101100101111111110010111111101111111110111110
"""