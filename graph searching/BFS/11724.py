from collections import deque
import sys
input=sys.stdin.readline
N, M = map(int,input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
visited = []
queue = deque()
for i in range(M):
    x, y = map(int,input().split())
    matrix[x][y] = matrix[y][x] = 1
global count
count = 0
def BFS(start, visit):
    if not start in visit:
        visit.append(start)
        queue.append(start)
        while queue:
            node = queue.popleft()
            for l in range(N+1):
                if matrix[node][l] and not (l in visit):
                    visit.append(l)
                    queue.append(l)
        global count
        count += 1
    else:
        return

for i in range(1, N+1):
    BFS(i, visited)
print(count)