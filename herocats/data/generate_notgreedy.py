#! /usr/env/python3

'''This test case should fail a naive greedy alg
that is going by most people saved until it hits limits of M/T.'''

M, T, N = 200, 100, 5

cases = [[10, 5, 10],
         [160, 100, 30],
         [20, 10, 12],
         [50, 50, 8],
         [10, 20, 6]]

print(*[M, T, N])
for case in cases:
    print(*case)
