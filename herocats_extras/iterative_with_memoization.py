#! /usr/bin/env python3
# INPUT

M, T, N = map(int, input().split())  # money, time, number of missions

missions = []  # list of tuples (cost, time, people_saved)

for _ in range(N):  # for each mission
    m, t, r = map(int, input().split())  # cost, time, people_saved
    missions.append((m, t, r))  # add tuple to list

# calculate efficiency for each mission
efficiencies = [(mission[2] / mission[0], mission) for mission in missions]
# sort missions based on efficiency in descending order
missions_sorted = sorted(efficiencies, key=lambda x: x[0], reverse=True)

# SOLUTION
memoization_table = [[0] * (T + 1) for _ in range(M + 1)]  # 2D array with size (M+1) x (T+1)

# Iterative solution:
for i in range(len(missions_sorted)):  # for each mission
    mission_cost, time_spend, people_saved = missions_sorted[i][1]  # get mission info
    for money_left in range(M, mission_cost - 1, -1):  # for each money_left
        for time_left in range(T, time_spend - 1, -1):  # for each time_left
            best = max(
                memoization_table[money_left][time_left],
                memoization_table[money_left - mission_cost][time_left - time_spend] + people_saved
            )  # skip mission or do mission
            memoization_table[money_left][time_left] = best  # update value in the memoization table

# OUTPUT
print(max(max(row) for row in memoization_table))  # print answer
