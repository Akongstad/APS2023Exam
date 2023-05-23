#! /usr/env/python3
from random import shuffle

'''Random solution that often but not always finds the correct solution.'''

def randompicker(M, T, N, missions):
    #print(missions)
    shuffle(missions) #O(N) time as uses fisher-yates shuffle alg
    #print(missions)
    m_t = 0
    t_t = 0
    r_t = 0

    for i in range(N): #O(N)
        m, t, r = missions[i]
        if m_t+m<=M and t_t+t<=T:
            m_t+=m
            t_t+=t
            r_t+=r
    
    return r_t


# Read the input values
M, T, N = map(int, input().split(' '))
missions = []
for _ in range(N):
    m, t, r = map(int, input().split(' '))
    missions.append((m, t, r))

# Generate random solutions and store them
x = []
for i in range(1000):
    x.append(randompicker(M, T, N, missions))

#Print best solution found
print(max(x))
