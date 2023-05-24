#! /usr/env/python3

'''This test case is difficult for the random solution to happen across the correct answer.'''

M, T, N = 100, 100, 49

cases = [[10,10,2]]*5+[[10,10,1]]*44
print(*[M, T, N])
for case in cases:
    print(*case)
