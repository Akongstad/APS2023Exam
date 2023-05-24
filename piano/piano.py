import time
from collections import defaultdict
from math import floor

WEEKEND = {6, 0}  # Saturday and Sunday


# Time complexity of ford-fulkerson: O(max_flow * E) worst case
# Max_flow in the worst case would be 2000.
# Runtime estimation:
# Worst case Edges: 1000 move_orders each with an edge to day 1 through 100. Each day has an edge to at max 1000 tuners.
# (1000 * 100) + (100 * 1000) = 110000 + 2000 from source and sink edges.
# 2000 * 110000 = 220.000.000 operations. Which is acceptable, but it needs to run 100 times in the worst case.
# TESTING:
# Sample execution on absolute worst case input():
# fine
# Total execution time:  9.68663406372 0703  s
# fine
# Total execution time:  9.724480867385864  s
# fine
# Total execution time:  9.905425071716309  s
# fine
# Total execution time:  10.036841869354248  s
# fine
# Total execution time:  9.835865020751953  s
# fine
# Total execution time:  9.896077156066895  s

# Build graph
# 2000*100*1000 = 200.000.000 operations


def dfs(s, t, parent, dfs_visited, skip_days):
    # Base case
    if s == t:
        return True
    dfs_visited[s] = True
    # Recursive loop
    for i in graph[s]:
        if not type(i) is tuple:
            if -1 < i < 101 and (i % 7) in skip_days:
                continue
        if not dfs_visited[i] and graph[s][i] > 0:
            parent[i] = s
            if dfs(i, t, parent, dfs_visited, skip_days):
                return True
    return False


# Find and return max flow from s to t in given graph
def flow(source, sink, skip_days):
    parent = defaultdict(lambda: -1)  # Stores path
    max_flow = 0

    # Augment flow while source -> sink exists
    while dfs(source, sink, parent, defaultdict(lambda: False), skip_days):
        # Find minimum residual capacity/O find the maximum flow through the path found.
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        # Add flow to max
        max_flow += path_flow

        # update residual capacities of the edges and reverse edges along the path.
        # Starting from the sink and going backwards through parent.
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow


def build_graph():
    # Build bipartite graph
    start_time = time.time()
    graph = defaultdict(lambda: defaultdict(int))
    for move in moves:  # For each move order
        graph[0][move] += 1  # Add source to move order
        for day in range(move[0], move[1] + 1):
            graph[move][day] += 1
            for tuner_i in range(1, floor(p / 2) + 1):
                tuner_i += 100  # Scale to make sure tuners and move orders are separate
                graph[day][tuner_i] = 1  # Add day to tuner
                graph[tuner_i][-1] = 100  # Add tuner to sink. 100 is capacity
    end_time = time.time()
    print("Total execution time: ", end_time - start_time, " s. Graph built.")


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        start_time = time.time()
        m, p = map(int, input().split())
        # graph is a dictionary of dictionaries
        # vertex -> (vertex -> capacity)
        graph = defaultdict(lambda: defaultdict(int))
        moves = [tuple(map(int, input().split())) for _ in range(m)]

        build_graph()
        new_start_time = time.time()
        only_weekdays = flow(0, -1, WEEKEND)
        new_end_time = time.time()
        print("Total execution time: ", new_end_time - new_start_time, " s. FF run.")
        # Check if any move order is not fulfilled
        if only_weekdays == m:
            print("fine")
            # end_time = time.time()
            # print("Total execution time: ", end_time - start_time, " s")
            continue
        with_weekends = flow(0, -1, set())
        if only_weekdays + with_weekends == m:
            print("weekend work")
            # end_time = time.time()
            # print("Total execution time: ", end_time - start_time, " s")
            continue
        print("serious trouble")
        # end_time = time.time()
        # print("Total execution time: ", end_time - start_time, " s")
