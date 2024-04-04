import sys

class Pair:
    def __init__(self, x, y):
        self.first = x
        self.second = y

def isSafe(mat, visited, x, y):
    return (x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and mat[x][y] != "#" and (not visited[x][y]))

def findShortestPath(mat, visited, i, j, x, y, min_dist, dist, path):
    if (i == x and j == y):
        if len(path) == 0 or len(dist) < len(path):
            path.clear()
            path.extend(dist)
        return

    visited[i][j] = True

    if (isSafe(mat, visited, i + 1, j)):
        dist.append("D")
        findShortestPath(mat, visited, i + 1, j, x, y, min_dist, dist, path)
        dist.pop()

    if (isSafe(mat, visited, i, j + 1)):
        dist.append("R")
        findShortestPath(mat, visited, i, j + 1, x, y, min_dist, dist, path)
        dist.pop()

    if (isSafe(mat, visited, i - 1, j)):
        dist.append("U")
        findShortestPath(mat, visited, i - 1, j, x, y, min_dist, dist, path)
        dist.pop()

    if (isSafe(mat, visited, i, j - 1)):
        dist.append("L")
        findShortestPath(mat, visited, i, j - 1, x, y, min_dist, dist, path)
        dist.pop()

    visited[i][j] = False

def findShortestPathLength(mat, src, dest):
    if (len(mat) == 0 or mat[src.first][src.second] == "#" or mat[dest.first][dest.second] == "#"):
        return ""

    row = len(mat)
    col = len(mat[0])

    visited = []
    for i in range(row):
        visited.append([False for _ in range(col)])

    dist = []
    path = []
    findShortestPath(mat, visited, src.first, src.second, dest.first, dest.second, float('inf'), dist, path)

    return "".join(path) if path else ""

maze = [
    [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
    [".", "#", ".", "#", ".", ".", ".", "#", ".", "."],
    [".", ".", ".", "#", ".", ".", "#", ".", "#", "."],
    ["#", "#", "#", "#", ".", "#", "#", "#", "#", "."],
    [".", ".", ".", "#", ".", ".", ".", "#", ".", "#"],
    [".", "#", ".", "B", ".", ".", "#", ".", "#", "#"],
    [".", "#", "#", "#", "#", "#", "#", "#", "#", "."],
    [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
    [".", ".", "#", "#", "#", "#", ".", "#", "#", "."],
    [".", ".", ".", "A", ".", ".", ".", ".", ".", "#"]
]

src = None
dest = None

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "A":
            src = Pair(i, j)
        elif maze[i][j] == "B":
            dest = Pair(i, j)

if src and dest:
    path = findShortestPathLength(maze, src, dest)
    if (path):
        print("Shortest Path is", path)
    else:
        print("Shortest Path doesn't exist")
else:
    print("Start or end point not found in the maze.")
