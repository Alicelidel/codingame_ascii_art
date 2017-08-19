import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def calc_distance(lat1, lon1, lat2, lon2):
    """Func to calc the distance between defib and the person"""
    x = (lon2 - lon1) * math.cos((lat1 + lat2) / 2)
    y = (lat2 - lat1)
    d = math.sqrt(x ** 2 + y ** 2) * 6371
    return d


def make_num(x):
    """Function to make RAD of DEG in str"""
    y = float(x.replace(",", "."))
    y = math.pi * y / 180
    return y


out_name = ''
out_dist = 100

lon = input()
lon1 = make_num(lon)

lat = input()
lat1 = make_num(lat)

n = int(input())
if n != 1:
    for i in range(n):
        num, name, addr, phone, lon2, lat2 = input().split(";")
        lon2 = make_num(lon2)
        lat2 = make_num(lat2)
        dist = calc_distance(lat1, lon1, lat2, lon2)
        if dist < out_dist:
            out_name = name
            out_dist = dist
if n == 1:
    num, name, addr, phone, lon2, lat2 = input().split(";")
    out_name = name

print(out_name)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

