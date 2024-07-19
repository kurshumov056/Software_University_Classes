'''


        Write a program to check whether a directed graph is acyclic or holds any cycles. The input ends with "End" line.

        Examples


Input                   Output

C-G                     Acyclic:  Yes
End



Input                   Output

A-F                     Acyclic: No
F-D
D-A
End

Input                   Output

E-Q                     Acyclic: Yes
Q-P
P-B
End




Input                   Output

                        Acyclic:

'''



from collections import deque

def dfs(node, graph, visited_graph):

    if graph:
        next_key = graph.popleft()
        visited_graph.append(next_key)

        if  not graph:
            if next_key[2] == visited_graph[0][0]:
                return 'Acycclic: No'
            else:
                return 'Acyclic: Yes'
        else:
            return dfs(next_key, graph, visited_graph)



command = ''
graph = deque()
visited_graph = deque()


while command != 'End':
    command = input('Please enter node connection: ')
    if command != 'End':
        graph.append(command)


result = dfs(graph[0], graph, visited_graph)
print('Final result', result)





