N = int(input())
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
count = 0
visit = [0 for _ in range(N+1)]
for i in range(int(input())):
    x, y = map(int,input().split())
    matrix[x][y] = matrix[y][x] = 1

def DFS(start, visited):
    visited[start] = 1
    for i in range(N+1):
        if matrix[start][i] and not visited[i]:
            DFS(i, visited)

DFS(1, visit)
for l in visit:
    if l:
        count += 1
print(count-1)