


'''

                                        4. Kruskals MST


If we have a weighted undirected graph, we can extract a sub-graph where all nodes (vertices) of the original
graph are connected by edges without any cycles. This is referred to as a spanning tree. A minimum spanning
tree (MST) is the spanning tree with the smallest weight (several MST could exist in some graphs).

For example, a cable operator wants to connect its customers to a cable network. The homes of the customers are connected by streets (edges) with different lengths (weights). To find out how to connect all homes to its network most efficiently (least distance covered) you need to find the MST. One simple algorithm to find the MST of a given graph is Kruskal’s algorithm.

Input

    · On the first line you will receive e – an integer – number of edges that you have to read.
    · On the next e lines, you will receive an edge in the following format: "{firstNode}, {seconNode}, {weight}".






Input               Output

11                  3 - 5
0, 3, 9             0 - 5
0, 5, 4             0 - 8
0, 8, 5             1 - 7
1, 4, 8             6 - 8
1, 7, 7             1 - 4
2, 6, 12            2 - 6
3, 5, 2
3, 6, 8
3, 8, 20
4, 7, 10
6, 8, 7


'''









from collections import deque

class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight



edges = 11 # input configured for debugging
graph = []
max_node = float('-inf')


first_second_weight = [
[0, 3, 9],
[0, 5, 4],
[0, 8, 5],
[1, 4, 8],
[1, 7, 7],
[2, 6, 12],
[3, 5, 2],
[3, 6, 8],
[3, 8, 20],
[4, 7, 10],
[6, 8, 7]
]

for row_input in first_second_weight:
    first, second, weight = [int(x) for x in row_input]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node

parent = [num for num in range(max_node + 1)]
forest = []


for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)
    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        forest.append (edge)

for edge in forest:
    print(f'{edge.first} - {edge.second}')


'''   
11
0, 3, 9
0, 5, 4
0, 8, 5
1, 4, 8
1, 7, 7
2, 6, 12
3, 5, 2
3, 6, 8
3, 8, 20
4, 7, 10
6, 8, 7


'''