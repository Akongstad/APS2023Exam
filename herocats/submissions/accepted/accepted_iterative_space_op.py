#! /usr/bin/env python3
def perform_missions(money_cap, time_cap, missions):
    num_missions = len(missions)
    dp = [[0] * (money_cap + 1) for _ in range(time_cap + 1)]

    for mission_i in range(1, num_missions + 1):
        cost, time_consumed, rescues = missions[mission_i - 1]
        for t in range(time_cap, time_consumed-1, -1):
            for m in range(money_cap, cost-1, -1):
                if cost <= m and time_consumed <= t:
                    perform_rescue = dp[t - time_consumed][m - cost] + rescues
                    dont_rescue = dp[t][m]
                    dp[t][m] = max(perform_rescue, dont_rescue)

    return dp[time_cap][money_cap]


if __name__ == '__main__':
    M, T, N = map(int, input().split())
    missions = []
    for i in range(N):
        missions.append(tuple(map(int, input().split())))

    rescues = perform_missions(M, T, missions)
    print(rescues)
