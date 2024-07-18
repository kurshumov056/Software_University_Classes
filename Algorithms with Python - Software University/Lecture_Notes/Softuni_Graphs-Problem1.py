



'''


1. Areas in Matrix

We are given a matrix of letters of size N * M. Two cells are neighbors if they share a common wall. Write a program
to find the connected areas of neighbor cells holding the same letter. Display the total number of areas and
the number of areas for each alphabetical letter (ordered by alphabetical order].
On the first line is given the number of rows.

Examples

Input                               Output

6
8

aacccaac                            Areas: 8
baaaaccc                            Letter 'a' -> 2
baabaccc                            Letter 'b' -> 2
bbdaaccc                            Letter 'c' -> 3
ccdccccc                            Letter 'd' -> 1
ccdccccc




'''







def dfs(parent, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if visited[row] [col]:
        return
    if matrix[row] [col] != parent:
        return

    visited[row][col] = True
    dfs(parent, row - 1, col, matrix, visited)
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)
    dfs(parent, row, col + 1, matrix, visited)

rows = int(input())
cols = int(input())

matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}



for row in range (rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row] [col]
        dfs(key, row, col, matrix, visited)
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1

print(areas)

'aacccaac',
'baaaaccc',
'baabaccc',
'bbdaaccc',
'ccdccccc',
'ccdccccc'