#!/bin/python3

import sys


S = input().strip()

try:
    s = int(S)
    print(S)
except:
    print('Bad String')
finally:
    pass