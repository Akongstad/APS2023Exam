#! /usr/env/python3

'''Greedy solution, will pass some inputs but not others'''
M, T, N = map(int, input().split(' '))
#print(M, N, T)
missions = [0]*N

for i in range(N):
    m, t, r = map(int, input().split(' '))
    #print(m, t, r)
    missions[i] = [r, m, t]

missions.sort(reverse=True)
people = 0
total_cost = 0
total_time = 0
for mission in missions:
    #print(mission)
    if (total_cost + mission[1] <= M) and (total_time + mission[2] <= T):
        #print('accepted')
        people += mission[0]
        total_cost +=  mission[1]
        total_time += mission[2]
    else: break

print(people)
