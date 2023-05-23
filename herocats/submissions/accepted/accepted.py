#! /usr/bin/env python3
def perform_missions(money_cap, time_cap, mission_i, missions, cache):
    if cache[mission_i][time_cap][money_cap] != -1:
        return cache[mission_i][time_cap][money_cap]

    if mission_i == 0 or money_cap == 0 or time_cap == 0:
        cache[mission_i][time_cap][money_cap] = 0
        return 0

    cost, time_consumed, rescues = missions[mission_i - 1]

    if cost > money_cap or time_consumed > time_cap:
        result = perform_missions(money_cap, time_cap, mission_i - 1, missions, cache)
        cache[mission_i][time_cap][money_cap] = result
        return result

    perform_rescue = perform_missions(money_cap - cost, time_cap - time_consumed, mission_i - 1, missions, cache) + rescues
    dont_rescue = perform_missions(money_cap, time_cap, mission_i - 1, missions, cache)
    result = max(perform_rescue, dont_rescue)

    cache[mission_i][time_cap][money_cap] = result
    return result


if __name__ == '__main__':
    M, T, N = map(int, input().split())
    missions = []
    for _ in range(N):
        missions.append(tuple(map(int, input().split())))

    cache = [[[-1 for _ in range(M + 1)] for _ in range(T + 1)] for _ in range(N + 1)]

    rescues = perform_missions(M, T, N, missions, cache)
    print(rescues)
