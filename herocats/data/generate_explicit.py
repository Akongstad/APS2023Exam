#! /usr/env/python3

'''This test case generates biggest possible test case
M=1999, T=499, N=49'''

import random
import sys
from math import floor, ceil

random.seed(42)
x, y, z, bound = map(int, sys.argv[1:-1])
print(x, y, z)

for _ in range(z):
    mission = [random.randrange(1, ceil(x / bound)),
               random.randrange(1, ceil(y / bound)),
               random.randrange(1, 50)]
    print(*mission)
