#! /usr/env/python3

'''This test case generates biggest possible test case
M=250, T=125, N=100'''

import random
import sys
from math import floor, ceil

random.seed(42)
x, y, z, bound = map(int, sys.argv[1:-1])
print(x, y, z)

for _ in range(z):
    mission = [random.randrange(1, ceil(x / bound)),
               random.randrange(1, ceil(y / bound)),
               random.randrange(1, 51)]
    print(*mission)
