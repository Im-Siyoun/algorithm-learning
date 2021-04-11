from collections import deque
N, M = map(int,input().split())
matrix = [[0]*M for i in range(N)]
visit = [[0]*M for i in range(N)]

for i in range(N):
    a = input().strip()
    for b, c in enumerate(a):
        matrix[i][b] = int(c)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

def BFS(y, x, visited):
    count = 1
    visited[y][x] = count
    queue.append([y,x,count])
    while queue:
        y, x, count = queue.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if matrix[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = count
                    queue.append([ny,nx,count])
    return visited[N-1][M-1]

print(BFS(0, 0, visit))