from collections import deque
N = int(input())
matrix = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]

for i in range(N):
    a = input().strip()
    for b, c in enumerate(a):
        matrix[i][b] = int(c)

queue = deque()
cnt = 0
num1 = 0
numlist = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(ny, nx, count, num):
    visited[ny][nx] = count
    queue.append([ny,nx])
    while queue:
        y, x = queue.popleft()
        num += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = count
                    queue.append([ny,nx])
    return num

for a in range(N):
    for b in range(N):
        if matrix[a][b] and not visited[a][b]:
            cnt += 1
            numlist.append(BFS(a, b, cnt, num1))
            num1 = 0

print(cnt)
numlist.sort()
for i in numlist:
    print(i)