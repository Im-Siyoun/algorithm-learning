from collections import deque
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
visit = []
matrix = []
def BFS(y,x):
    queue = deque()
    visit[y][x] = 1
    queue.append([y, x])
    while queue:
        y, x = queue.popleft()
        for v in range(8):
            nx = x + dx[v]
            ny = y + dy[v]
            if 0 <= nx < w and 0 <= ny < h:
                if matrix[ny][nx] and not visit[ny][nx]:
                    queue.append([ny,nx])
                    visit[ny][nx] = 1

while True:
    w,h = map(int,input().split())
    if not w and not h:
        break
    matrix = []
    count = 0
    for i in range(h):
        matrix.append(list(map(int,input().split())))
    visit = [[0]*w for _ in range(h)]
    for i in range(h):
        for l in range(w):
            if matrix[i][l] and not visit[i][l]:
                BFS(i,l)
                count += 1
    print(count)