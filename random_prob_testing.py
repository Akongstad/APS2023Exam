from random import randint
from math import factorial
import sys
import matplotlib.pyplot as plt
from scipy.stats import binom

def single_trial(x, m):
    ''' A single Bernoulli trial where:
        x = number of missions needing to be chosen
        m = total number of missions
        Returns p, the chance of a success'''

    return (factorial(x)*factorial(m-x))/factorial(m)

def multi_trials(x, m, n):
    '''Returns the chances of at least one successful trial
        x = number of missions needing to be chosen
        m = total number of missions
        n = number of trials'''

    #calculate p
    p = single_trial(x, m)
    #model binomial RV with p and n
    
    #chance of zero successful trials
    fail = binom.pmf(0, n, p) 

    #chance of at least one successful trial as this means it will give the correct answer
    return(1-fail) 

if __name__ == '__main__':
    # x number of missions needed to be chosen correctly to get the correct answer
    # m number of missions in total
    # n number of trials
    # Assumes there is only one possible correct 'set' of missions
    x, m, n = map(int, sys.argv[1:4])

    print(multi_trials(x, m, n))

    dist = [0]*m
    #make distribution
    for i in range(1,m+1):
        #print()
        #print('new trial: ', i, m, n)
        dist[i-1] = [i, multi_trials(i, m, n)]
    print(dist)

    plt.plot([x[0] for x in dist],[x[1] for x in dist])
    plt.xlabel("Number missions in the 'correct' set" )
    plt.ylim(-0.1,1.1)
    plt.ylabel("P(x)")
    #plt.title("Probabilities of wa_random.py returning correct solution")
    plt.savefig(f"random_dist{m}.png")
    plt.show()