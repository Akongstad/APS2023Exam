## THIS IS A TEMPLATE FROM THE MANDATORY ASSIGNMENT
#! /usr/env/python3

import random
import sys

random.seed(int(sys.argv[-1])) 

def test_case():
    M = random.randrange(1, 2000)
    T = random.randrange(1, 500)
    N = random.randrange(1, 50) 

    first_line = [M, T, N]

    print(*first_line)
    
    for _ in range(N):
        m = random.randrange(1, M+1)
        t = random.randrange(1, T+1)
        r = random.randrange(1,100)
        mission = [m, t, r]
        print(*mission)


if __name__ == '__main__':
    test_case()
