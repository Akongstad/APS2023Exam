#Idea:
#create a graph
#pass through nodes (O(N))
#check if coloured already
#navigate graph (BFS or DFS? Maybe it doesn't matter? 
#Both O(N+E) in worst case?)
#and colour alternatively as you go. 
#If disconnected, colour one part fully before jumping to another part.
#If graph can be fully coloured, then it is possible 
#to divide list between Walter and Jesse
#else it is not.

### DFS recursive implementation
## Hits recursion depth in largest cases

class Graph():
    def __init__(self, N):
        self.nodes = dict()
        self.node_list = [0]*N

    def add_node(self, node):
        self.nodes[node] = []

    def add_neighbours(self, u, v):
        self.nodes[u].append(v)
        self.nodes[v].append(u)


def dfs(graph, node, assigned, walters, jesses):
    col = assigned[node]
    oth_col = 'Jesse' if col == 'Walter' else 'Walter'
    
    if col == 'Walter':
        walters.append(node)
    else:
        jesses.append(node)
    
    for neighbour in graph.nodes[node]:
        if neighbour not in assigned:
            assigned[neighbour] = oth_col
            dfs(graph, neighbour, assigned, walters, jesses)
        elif assigned[neighbour] == col:
            print('impossible')
            exit()

def is_bipartite(graph, N):
    assigned = dict()
    walters = []
    jesses = []

    for i in range(N):
        source = graph.node_list[i]
        if source not in assigned:
            assigned[source] = 'Walter'
            dfs(graph, source, assigned, walters, jesses)

    print(*walters)
    print(*jesses)
    #return True


# Get number of items
N = int(input())
my_graph = Graph(N)

# Add the items as nodes in the graph
for i in range(N):
    n = input()
    my_graph.add_node(n)
    my_graph.node_list[i] = n

# Get number of sus pairs
M = int(input())
# Add the sus pairs as neighbors to nodes
for j in range(M):
    u, v = input().split()
    my_graph.add_neighbours(u, v)

is_bipartite(my_graph, N)
