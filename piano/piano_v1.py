# 8.4a, Network Flow, Standard
from collections import defaultdict, deque
from math import floor

# Piano tuners always work in pairs. They can move at most one piano per day.

# Input:
# n <= 100 test cases
# Each test case:
# m <= 1000(pianos to be moved) and p <= 2000 (Piano tuners)
# m lines of move orders:
# bi and ei with 1 <= bi < ei <= 100.
# Between the beginnig day bi and the end day ei, piano i must be moved

# Output:
# "serious trouble" if there is no solution
# "weekend work" if at least 2 piano tuners have to work on the weekend
# "fine" if all pianos can be moved without weekend work

# Idea:
# I want to match piano movers with move orders.
# Edmond Karp's algorithm with BFS vs DFS.
# O(E*F). DFS pitfall time complexity depends on the capacity values of the edges. We might only ever be able to push 1 unit og flow in each iteration.
# BFS. O(V*E^2). Each iteration takes O(E) time. We can have at most O(E) iterations. Each iteration we can find an augmenting path in O(V) time. Strongly polynomial time algorithm.
# Using BFS ensures that we find the shortest length augmenting path.

# I will implement skip days into the bfs search. The first time we find a path to a day that is not a weekend, we will use that path.
# If the max flow is less than the number of move orders, we have a problem. We try again, but with weekends.
# What if duplicate move orders example: [91,91] and [91,91]? We can just add the capacity of the edge.?
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

# Edmond-karp bfs based
# Return true if there is a path from s to t
def bfs(s, t, parent, skip_days):
    visited = set()
    queue = deque()

    # Mark s as visited
    queue.append(s)
    visited.add(s)

    # BFS loop
    while queue:
        # u = Dequeue element
        u = queue.popleft()
        # Get all adj V's of u. If not visited mark and enqueue it
        for cur_target in graph[u]:
            if not type(cur_target) is tuple:
                if -1 < cur_target < 101 and (cur_target % 7) in skip_days:
                    continue
            if cur_target not in visited and graph[u][cur_target] > 0:
                queue.append(cur_target)
                visited.add(cur_target)
                parent[cur_target] = u
    # If we reached sink in BFS starting from source, then true else false
    return t in visited


# Find and return max flow from s to t in given graph
# Edmond-karp bfs based O(V*E^2). Does not depend on the capacity values of the edges.
def flow(source, sink, skip_days):
    parent = defaultdict(lambda: -1)  # Stores path
    max_flow = 0

    # Augment flow while source -> sink exists
    #while bfs(source, sink, parent, skip_days):
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
                for tuner_i in range(1, floor(p/2)+1):
                    tuner_i += 100 # Scale to make sure tuners and move orders are seperate
                    graph[day][tuner_i] = 1  # Add day to tuner
                    graph[tuner_i][-1] = 100  # Add tuner to sink. 100 is maximum
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
        # Check if weekend work
