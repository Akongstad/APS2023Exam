#! /usr/env/python3

'''This test case can be solved with a greedy alg.'''

M, T, N = 200, 100, 5

cases = [[10, 5, 10],
         [100, 80, 3],
         [20, 10, 12],
         [50, 50, 8],
         [10, 20, 6]]

print(*[M, T, N])
for case in cases:
    print(*case)
