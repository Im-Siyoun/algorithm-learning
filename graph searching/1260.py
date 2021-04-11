import sys
input=sys.stdin.readline

def DFS(start, visit):
    visit[start] = 1
    print(start, end=' ')
    for v in range(N+1):
        if visit[v] == 0 and matrix[start][v]:
            DFS(v, visit)

def BFS(start, visit):
    visit[start] = 0
    queue.append(start)
    while queue:
        start = queue[0]
        del queue[0]
        print(start,end=' ')
        for v in range(N+1):
            if visit[v] == 1 and matrix[start][v]:
                visit[v] = 0
                queue.append(v)

N, M, V = map(int,input().split())
matrix = []
queue = []
visited = [0 for _ in range(N+1)]
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1
DFS(V, visited)
print()
BFS(V, visited)