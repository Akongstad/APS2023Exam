import functools


@functools.cache
def perform_missions(money_cap, time_cap, mission_i):
    # Base case 1
    if money_cap == 0 or time_cap == 0 or mission_i == 0:
        return 0

    # Base case 2
    if missions[mission_i - 1][0] > money_cap or missions[mission_i - 1][1] > time_cap:
        return perform_missions(money_cap, time_cap, mission_i - 1)

    # Recursive loop
    cost, time_consumed, rescues = missions[mission_i - 1]

    perform_rescue = perform_missions(money_cap - cost, time_cap - time_consumed, mission_i - 1) + rescues
    dont_rescue = perform_missions(money_cap, time_cap, mission_i - 1)

    return max(perform_rescue, dont_rescue)


if __name__ == '__main__':
    M, T, N = map(int, input().split())
    missions = []
    for i in range(N):
        missions.append(tuple(map(int, input().split())))  # Map with move span
    rescues = perform_missions(M, T, len(missions))
    print(rescues)
