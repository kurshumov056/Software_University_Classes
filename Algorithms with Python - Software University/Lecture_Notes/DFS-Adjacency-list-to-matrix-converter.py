'''nodes = int(input())

graph = {}
edges = [|]
for _ in range (nodes):
    node, children_str = input().split(" -> ")
    children = children_str.split()
    graph[node] = children'''


def dfs_matrix(v, graph, visited):
    visited[v] = True
    print(v, end=' ')
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and not visited[i]:
            dfs_matrix(i, graph, visited)

graph = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 1]
]
visited = [False] * len(graph)
dfs_matrix(0, graph, visited)


# Convert the adjacency list to an adjacency matrix
def convert_to_matrix(graph):
    nodes = list(graph.keys())
    size = len(nodes)
    index = {nodes[i]: i for i in range(size)}
    matrix = [[0] * size for _ in range(size)]

    for node, edges in graph.items():
        for edge, weight in edges:
            matrix[index[node]][index[edge]] = weight
            current_matrix_input = matrix[index[node]][index[edge]]

    return matrix


# Example usage
graph_list = {
    'A': [('B', 2), ('C', 1)],
    'B': [('C', 3)],
    'C': [('A', 4)]
}

graph_matrix = convert_to_matrix(graph_list)
print("Adjacency Matrix:")
for row in graph_matrix:
    print(row)

# DFS traversal
visited = [False] * len(graph_matrix)
dfs_matrix(0, graph_matrix, visited)
