from collections import deque
n = int(input())
matrix = [[0]*(n+1) for _ in range(n+1)]
a, b = map(int,input().split())

for i in range(int(input())):
    x, y = map(int,input().split())
    matrix[x][y] = matrix[y][x] = 1

visit = [0]*(n+1)
queue = deque()

def BFS(start):
    chone = 0
    queue.append(start)
    visit[start] = chone
    while queue:
        node = queue.popleft()
        chone = visit[node] + 1
        for i in range(n+1):
            if matrix[node][i] and not visit[i]:
                queue.append(i)
                visit[i] = chone

BFS(a)
if not visit[b]:
    print(-1)
else:
    print(visit[b])