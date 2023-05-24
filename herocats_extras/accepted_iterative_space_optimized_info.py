# we can optimize the dynamic programming solution by using a 2D array instead of a 3D array. Since the current state
# only depends on the previous state, we can reduce the space complexity.
# we use a 2D array dp where dp[t][m] represents the maximum number of rescues that can be obtained with t
# time remaining and m money remaining. We iterate in reverse order for t and m to ensure that we are using the previously calculated values from the same iteration.

# By making this modification, we eliminate the need for the third dimension in the dp array,
# reducing the space complexity from O(N * T * M) to O(T * M).
import sys


def perform_missions(money_cap, time_cap, missions):
    num_missions = len(missions)
    dp = [[0] * (money_cap + 1) for _ in range(time_cap + 1)]
    chosen = [[[] for _ in range(money_cap + 1)] for _ in range(time_cap + 1)]

    for mission_i in range(1, num_missions + 1):
        cost, time_consumed, rescues = missions[mission_i - 1]
        for t in range(time_cap, time_consumed - 1, -1):
            for m in range(money_cap, cost - 1, -1):
                if cost <= m and time_consumed <= t:
                    perform_rescue = dp[t - time_consumed][m - cost] + rescues
                    dont_rescue = dp[t][m]

                    if perform_rescue > dont_rescue:
                        dp[t][m] = perform_rescue
                        chosen[t][m] = chosen[t - time_consumed][m - cost] + [mission_i]
                    else:
                        dp[t][m] = dont_rescue
                        chosen[t][m] = chosen[t][m]

    max_rescues = dp[time_cap][money_cap]
    chosen_missions = chosen[time_cap][money_cap]
    return max_rescues, chosen_missions


if __name__ == '__main__':
    M, T, N = map(int, input().split())
    missions = []
    for i in range(N):
        missions.append(tuple(map(int, input().split())))

    rescues, chosen_missions = perform_missions(M, T, missions)

    print("Maximum rescues:", rescues)

    total_money = 0
    total_time = 0
    for mis in chosen_missions:
        cost, time_consumed, _ = missions[mis - 1]
        total_money += cost
        total_time += time_consumed
    print("Money spent:", total_money)
    print("Time spent:", total_time)
    print("Chosen missions:", chosen_missions)
