#! /usr/env/python3

'''This test case generates biggest possible test case
50M=1999, T=499, N=49'''

import random
random.seed(42)
print("1999 499 49")

for _ in range(49):
    mission = [random.randrange(1, 2000), 
               random.randrange(1,500), 
               random.randrange(1,50)]
    print(*mission)
