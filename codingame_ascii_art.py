import sys
import math


# usual input:
# 4
# 5
# E, MANHATTAN
# _ #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ###
# _# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   #
# _### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ##
# _# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #
# _# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #

def get_let(m1, m2, h, l, n):
    text = ''
    for row in m1:
        stroka = row
        text = str(stroka[l * (n):(l * (n + 1)) - 1])
        m2.append(text)


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
text = t.upper()
num = len(t)
asci_input = []
asci_output = []
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
m = len(chars)
for i in range(h):
    row = input()
    asci_input.append(row)

for t in text:
    if t not in chars:
        index = 26
        get_let(asci_input, asci_output, h, l, index)
    if t in chars:
        index = chars.index(t)
        get_let(asci_input, asci_output, h, l, index)


for i in range(h):
    text = ''
    for row in asci_output[i::5]:
        text += row + ' '
    print(text)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)