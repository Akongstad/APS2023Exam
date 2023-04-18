## THIS IS A TEMPLATE FROM THE MANDATORY ASSIGNMENT
#! /usr/env/python3

import random
import sys

random.seed(int(sys.argv[-1])) 

n = random.randrange(3, 300)
print(n)

for _ in range(n-1):
    print(random.randrange(-10000, 10000), end=" ")
print(random.randrange(-10000, 10000), end="")
print("")