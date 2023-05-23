#! /usr/bin/env python3
def perform_missions(money_cap, time_cap, missions):
    max_rescues = [[0 for _ in range(time_cap + 1)] for _ in range(money_cap + 1)]

    for i in range(len(missions)):
        cost, time_consumed, rescues = missions[i]
        for j in range(money_cap, cost - 1, -1):
            for k in range(time_cap, time_consumed - 1, -1):
                max_rescues[j][k] = max(max_rescues[j][k], max_rescues[j - cost][k - time_consumed] + rescues)

    return max_rescues[money_cap][time_cap]


if __name__ == '__main__':
    M, T, N = map(int, input().split())
    missions = []
    for _ in range(N):
        missions.append(tuple(map(int, input().split())))

    rescues = perform_missions(M, T, missions)
    print(rescues)
