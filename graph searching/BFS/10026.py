from collections import deque
visit = []
matrix = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(y,x,color):
    queue = deque()
    visit[y][x] = color
    queue.append([y,x])
    while queue:
        y, x = queue.popleft()
        for v in range(4):
            ny = y + dy[v]
            nx = x + dx[v]
            if 0 <= ny < N and 0 <= nx < N:
                if matrix[ny][nx] == color and not visit[ny][nx]:
                    visit[ny][nx] = color
                    queue.append([ny,nx])

def BFS1(y,x,color):
    queue = deque()
    if color == 'R' or color == 'G':
        queue.append([y,x])
        while queue:
            y,x = queue.popleft()
            for v in range(4):
                ny = y + dy[v]
                nx = x + dx[v]
                if 0 <= ny < N and 0 <= nx < N:
                    if (matrix[ny][nx] == 'R' or matrix[ny][nx] == 'G') and not visit[ny][nx]:
                        visit[ny][nx] = 'Y'
                        queue.append([ny,nx])
    else:
        BFS(y,x,color)

count = 0
N = int(input())
for i in range(N):
    matrix.append(list(input()))
visit = [[0]*N for _ in range(N)]
for i in range(N):
    for l in range(N):
        if not visit[i][l]:
            BFS(i, l, matrix[i][l])
            count += 1
visit = [[0]*N for _ in range(N)]
print(count, end = ' ')
count = 0        
for i in range(N):
    for l in range(N):
        if not visit[i][l]:
            BFS1(i,l,matrix[i][l])
            count += 1
print(count)