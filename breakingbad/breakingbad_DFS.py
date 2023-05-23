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

### DFS implementation

class Graph():
    def __init__(self, N):
        self.nodes = dict()
        self.node_list = [0]*N
    
    def add_node(self, node):
        self.nodes[node] = []

    def add_neighbours(self, u,v):
        self.nodes[u].append(v)
        self.nodes[v].append(u)


def is_bipartite(graph, N):
    assigned = dict()
    walters = []
    jesses = []
    for i in range(N):
        #print(assigned)
        source = graph.node_list[i]
        if source not in assigned:
            #assign source
            assigned[source] = 'Walter'
            #to hold visit list:
            to_visit = [source]
            

            while len(to_visit) > 0:
                #print('visit list: ', to_visit)
                curr = to_visit.pop()
                #print('current node', curr)
                col = assigned[curr]
                oth_col = 'Jesse' if col == 'Walter' else 'Walter'
                if col == 'Walter':
                    walters.append(curr)
                else:
                    jesses.append(curr)

                for neighbour in graph.nodes[curr]:
                    if neighbour not in assigned:
                        assigned[neighbour] = oth_col
                        to_visit.append(neighbour)
                    elif assigned[neighbour] == col:
                        print('impossible')
                        return False

    print(*walters)
    print(*jesses)
    return True


#get number of items
N = int(input())
my_graph = Graph(N)

#add the items as nodes in graph
for i in range(N):
    n = input()
    my_graph.add_node(n)
    my_graph.node_list[i] = n

#print(my_graph.nodes)

#get number of sus pairs
M = int(input())
#add the sus pairs as neighbours to nodes
for j in range(M):
    u,v = input().split()
    #print(u, v)
    my_graph.add_neighbours(u,v)

#print(my_graph.nodes)

is_bipartite(my_graph, N)
