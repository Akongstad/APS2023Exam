from collections import defaultdict
from collections import deque
from math import floor

WEEKEND = {6, 0}  # Saturday and Sunday

# Dinic's algorithm based implementation. O(V^2*E) runtime worst case.

def bfs(adj, s, t, level, skip_days):
    queue = deque()
    queue.append(s)
    level[s] = 0
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not type(v) is tuple:
                if -1 < v < 101 and (v % 7) in skip_days:
                    continue
            if level[v] == -1 and adj[u][v] > 0:
                level[v] = level[u] + 1
                queue.append(v)
    return level[t] != -1


def dfs(adj, u, t, flow, level, visited, skip_days):
    if u == t:
        return flow
    for v in adj[u]:
        if not type(v) is tuple:
            if -1 < v < 101 and (v % 7) in skip_days:
                continue
        if visited[v] or level[v] != level[u] + 1 or adj[u][v] <= 0:
            continue
        visited[v] = True
        current_flow = min(flow, adj[u][v])
        delta = dfs(adj, v, t, current_flow, level, visited, skip_days)
        if delta > 0:
            adj[u][v] -= delta
            adj[v][u] += delta
            return delta
    return 0


# Returns the maximum flow from s to t in the given graph
# dinic's algorithm
def flow(s, t, adj, skip_days):
    n = len(adj)
    max_flow = 0
    level = defaultdict(lambda: -1)
    while bfs(adj, s, t, level, skip_days):
        flow = dfs(adj, s, t, float('inf'), level, defaultdict(lambda: False), skip_days)
        while flow:
            max_flow += flow
            flow = dfs(adj, s, t, float('inf'), level, defaultdict(lambda: False), skip_days)
        level = defaultdict(lambda: -1)
    return max_flow


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

        # Build bipartite graph
        for move_i in moves:  # For each move order
            graph[0][move_i] += 1  # Add source to move order
            for day in range(move_i[0], move_i[1] + 1):
                graph[move_i][day] += 1
                for tuner_i in range(1, floor(p / 2) + 1):
                    tuner_i += 100  # Scale to make sure tuners and move orders are seperate
                    graph[day][tuner_i] = 1  # Add day to tuner
                    graph[tuner_i][-1] = 100  # Add tuner to sink. 100 is maximum
        only_weekdays = flow(0, -1, graph, WEEKEND)
        # Check if any move order is not fulfilled
        if only_weekdays == m:
            print("fine")
            continue
        with_weekends = flow(0, -1, graph, set())
        if only_weekdays + with_weekends == m:
            print("weekend work")
            continue
        print("serious trouble")
        # Check if weekend work
