#! /usr/env/python3

import random
import sys

random.seed(int(sys.argv[-1]))

def test_case():
    '''This generates a random test case for herocats'''
    M = random.randrange(1, 251)
    T = random.randrange(1, 126)
    N = random.randrange(1, 101)

    print(*[M, T, N])
    
    for _ in range(N):
        m = random.randrange(1, M+1)
        t = random.randrange(1, T+1)
        r = random.randrange(1, 51)

        print(*[m, t, r])


if __name__ == '__main__':
    test_case()
