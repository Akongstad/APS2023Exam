#! /usr/env/python3

import random
import sys

def test_case():
    '''Takes 4 numbers from sys.argv, M, T, N and seed.
    prints M T N
    prints N random test cases'''
    M,T,N,s = map(int, sys.argv[1:])
    random.seed(s)
    
    print(*[M, T, N])
    
    ## get proportions to scale outputs
    #M: 100/2000 = 0.05
    #T: 100/500 = 0.2
    #weighting 0.4M + 0.8T

    for _ in range(N):
        m = random.randrange(1, M+1)
        t = random.randrange(1, T+1)
        M_ = m*0.05
        T_ = t*0.2
        R = int(0.4*M_ + 0.6*T_) #Creates proportional R values
        if R < 20: # protects against silly numbers for very low M/Ts
            R = 20

        #number of people generated is now proportional 
        #to money and time available, unless M&T are small
        r = random.randrange(0, R)
        print(*[m, t ,r])


if __name__ == '__main__':
    test_case()
