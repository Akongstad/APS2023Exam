from collections import defaultdict, deque
from math import floor

WEEKEND = {6, 0}  # Saturday and Sunday


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
    # while bfs(source, sink, parent, skip_days):
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
    for move_i in moves:  # For each move order
        graph[0][move_i] += 1  # Add source to move order
        for day in range(move_i[0], move_i[1] + 1):
            graph[move_i][day] += 1
            for tuner_i in range(1, floor(p / 2) + 1):
                tuner_i += 100  # Scale to make sure tuners and move orders are seperate
                graph[day][tuner_i] = 1  # Add day to tuner
                graph[tuner_i][-1] = 100  # Add tuner to sink. 100 is capacity


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        m, p = map(int, input().split())
        # graph is a dictionary of dictionaries
        # vertex -> (vertex -> capacity)
        graph = defaultdict(lambda: defaultdict(int))
        moves = []
        for _ in range(m):
            moves.append(tuple(map(int, input().split())))  # Map with move span

        build_graph()
        only_weekdays = flow(0, -1, WEEKEND)
        # Check if any move order is not fulfilled
        if only_weekdays == m:
            print("fine")
            continue
        with_weekends = flow(0, -1, set())
        if only_weekdays + with_weekends == m:
            print("weekend work")
            continue
        print("serious trouble")
