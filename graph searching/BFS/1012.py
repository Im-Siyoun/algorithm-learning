from collections import deque
bx = [-1, 1, 0, 0]
by = [0, 0, -1, 1]

def BFS(y, x, visited, count):
    visited[y][x] = count
    queue.append([y,x])
    while queue:
        y, x = queue.popleft()
        for v in range(4):
            nx = x + bx[v]
            ny = y + by[v]
            if 0 <= nx < M and 0 <= ny < N:
                if matrix[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = count
                    queue.append([ny,nx])

for i in range(int(input())):
    queue = deque()
    result = 0
    M, N, K = map(int,input().split())
    matrix = [[0]*M for i in range(N)]
    visit = [[0]*M for i in range(N)]
    for l in range(K):
        a,b = map(int,input().split())
        matrix[b][a] = 1
    for a in range(N):
        for b in range(M):
            if matrix[a][b] and not visit[a][b]:
                result += 1
                BFS(a, b, visit, result)
                
    print(result)