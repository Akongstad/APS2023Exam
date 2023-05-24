# add your bruteforce solution here
import heapq
from math import floor


def can_move(tuners, moves, skip_days):
    move_i = 0
    end_times = []
    for day in range(1, 101):
        while move_i < len(moves) and moves[move_i][0] <= day:
            heapq.heappush(end_times, moves[move_i][1])
            move_i += 1
        if day % 7 not in skip_days:
            for _ in range(floor(tuners / 2)):
                if not end_times:
                    break
                heapq.heappop(end_times)
        if end_times and end_times[0] <= day:
            return False
        if not end_times and move_i == len(moves):
            break
    return True


if __name__ == '__main__':
    # start_time = time.time()
    T = int(input())
    for _ in range(T):
        N, P = map(int, input().split())
        moves = sorted([tuple(map(int, input().split())) for _ in range(N)])

        if can_move(P, moves, {0, 6}):
            print("fine")
            continue
        elif can_move(P, moves, set()):
            print("weekend work")
            continue
        print("serious trouble")

# end_time = time.time()
# print("Total execution time: ", end_time - start_time, " s")
