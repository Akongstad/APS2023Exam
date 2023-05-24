#! /usr/env/python3

'''Correct but slow'''
M, T, N = map(int, input().split(' '))
#print(M, N, T)

solutions = [[0,0,0]]

#print(solutions)
for i in range(N):
    m, t, r = map(int, input().split(' '))
    #print(m, t, r)
    for j in range(len(solutions)):
        solutions.append([solutions[j][0]+r, solutions[j][1]+m, solutions[j][2]+t])
        
solutions.sort(reverse=True)
#print(solutions)

for p, m, t in solutions:
    if m <= M and t <=T:
        print(p)
        break
