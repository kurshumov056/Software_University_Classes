'''

18
0, 6, 10
0, 8, 12
6, 4, 17
6, 5, 6
8, 5, 3
5, 4, 5
5, 11, 33
8, 2, 14
2, 11, 9
2, 7, 15
4, 1, 20
4, 11, 11
11, 1, 6
11, 7, 20
1, 9, 5
1, 7, 26
7, 9, 3
3, 10, 7
0
9

'''

'''
                            2. Dijkstra's Algorithm

Finding the shortest path between two nodes in an unweighted graph is done by applying simple BFS. 
When we’re working with weighted graphs though, things get more complicated. Dijkstra’s algorithm 
is one of the most famous ones that solve this task. A classical application of the shortest path 
algorithm might be to find the shortest path between two towns on a map holding towns connected with 
roads where each road holds the distance between two towns. In this problem, we’ll try to implement the 
optimized version of Dijkstra’s algorithm using a priority queue. Example: Find the shortest path 
between node 0 and node 9 in the following weighted undirected graph: 


Input
    . On the first, you will receive an integer - e - number of edges.
    . On the next e lines, you will receive an edge in the following format: "{start}, {end}, {weight}".
    . On the next line, you will receive a start node.
    . On the last line, you will receive an end node.

Output
    . Print the cost of the shortest path.
    . Print all nodes that form the shortest path.
    . If the end node can't be reached from the start node, then you have to print: "There is no such
    path,"

1
Input                   Output

18                      42
0, 6, 10                0 8 5 4 11 1 9
0, 8, 12
6, 4, 17
6, 5, 6
8, 5, 3
5, 4, 5
5, 11, 33
8, 2, 14
2, 11, 9
2, 7, 15
4, 1, 20
4, 11, 11
11, 1, 6
11, 7, 20
1, 9, 5
1, 7, 26
7, 9, 3
3, 10, 7
0
9



'''
graph = {}
edges = 18
source_destination_weight = [
    [0, 6, 10],
    [0, 8, 12],
    [6, 4, 17],
    [6, 5, 6],
    [8, 5, 3],
    [5, 4, 5],
    [5, 11, 33],
    [8, 2, 14],
    [2, 11, 9],
    [2, 7, 15],
    [4, 1, 20],
    [4, 11, 11],
    [11, 1, 6],
    [11, 7, 20],
    [1, 9, 5],
    [1, 7, 26],
    [7, 9, 3],
    [3, 10, 7]
]


from queue import PriorityQueue
from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight




for row_input in source_destination_weight:
    source, destination, weight = [int(x) for x in row_input]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))

start = 0
target = 9

max_node = max(graph.keys())

distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == target:
        break

    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            pq.put((new_distance, edge.destination))

if distance[target] == float('inf'):
    print('There is no such path.')
else:
    print(distance[target])

    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')



