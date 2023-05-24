import sys

def perform_missions(money_cap, time_cap, missions):
    num_missions = len(missions)
    dp = [[0] * (money_cap + 1) for _ in range(time_cap + 1)]

    for mission_i in range(1, num_missions + 1):
        cost, time_consumed, rescues = missions[mission_i - 1]
        for t in range(time_cap, time_consumed-1, -1):
            for m in range(money_cap, cost-1, -1):
                perform_rescue = dp[t - time_consumed][m - cost] + rescues
                dont_rescue = dp[t][m]
                dp[t][m] = max(perform_rescue, dont_rescue)

    return dp[time_cap][money_cap]


if __name__ == '__main__':
    M, T, N = map(int, sys.stdin.readline().split())
    missions = []
    for _ in range(N):
        missions.append(tuple(map(int, sys.stdin.readline().split())))

    rescues = perform_missions(M, T, missions)
    print(rescues)
