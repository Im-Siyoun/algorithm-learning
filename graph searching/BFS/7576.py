from collections import deque
import sys
input=sys.stdin.readline
queue = deque()
N, M = map(int,input().split())
matrix = []
visit = []
for i in range(M):
    tmp = list(map(int,input().split()))
    visit.append(tmp)
    matrix.append(tmp)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(y, x, count, visited):
    queue.append([y, x, count])
    while queue:
        y, x, count = queue.popleft()
        visited[y][x] = count
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[ny][nx] == -1:
                    visited[ny][nx] = -1
                elif matrix[ny][nx] == 0:
                    if not visited[ny][nx] or visited[ny][nx] > count:
                        queue.append([ny, nx, count])

for l in range(M):
    for v in range(N):
        if matrix[l][v] == 1:
            BFS(l, v, matrix[l][v], visit)
mx = 0
nc = False
for l in range(M):
    if 0 in visit[l]:
        nc = True
        break
    for v in visit[l]:
        if v > mx:
            mx = v
if nc:
    print(-1)
elif mx == 1:
    print(0)
else:
    print(mx-1)