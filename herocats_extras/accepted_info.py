import sys

sys.setrecursionlimit(10 ** 6)
CACHE = {}


def perform_missions(money_cap, time_cap, mission_i):
    # Base case 1
    if money_cap == 0 or time_cap == 0 or mission_i == 0:
        return 0, []

    if (mission_i, time_cap, money_cap) in CACHE and CACHE[(mission_i, time_cap, money_cap)] != -1:
        return CACHE[(mission_i, time_cap, money_cap)]

    # Base case 2
    if missions[mission_i - 1][0] > money_cap or missions[mission_i - 1][1] > time_cap:
        result = perform_missions(money_cap, time_cap, mission_i - 1)
        CACHE[(mission_i, time_cap, money_cap)] = result
        return result

    # Recursive loop
    cost, time_consumed, rescues = missions[mission_i - 1]

    perform_rescue = perform_missions(money_cap - cost, time_cap - time_consumed, mission_i - 1)
    perform_rescue = (perform_rescue[0] + rescues, perform_rescue[1] + [mission_i])
    dont_rescue = perform_missions(money_cap, time_cap, mission_i - 1)
    result = max(perform_rescue, dont_rescue)

    CACHE[(mission_i, time_cap, money_cap)] = result
    return result


if __name__ == '__main__':
    M, T, N = map(int, input().split())
    missions = []
    for i in range(N):
        missions.append(tuple(map(int, input().split())))

    rescues, chosen_missions = perform_missions(M, T, len(missions))

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
