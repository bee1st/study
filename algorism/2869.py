import sys
import math
x = list(map(int, sys.stdin.readline().split()))

A = x[0]
B = x[1]
V = x[2]

d = (V - A) / (A - B)
day = math.ceil(d)
print(day + 1)