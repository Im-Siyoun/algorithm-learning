import sys
from collections import deque
input=sys.stdin.readline

def DFS(q,m,graph):
    while True:
        i, time = q.popleft()
        graph[i] = 1
        if i == m: return time
        for l in (i-1, i+1, i*2):
            if 0<=l<100001 and not graph[l]:
                q.append((l, time+1))
    DFS(q, m, graph)

n, m = map(int,input().split())
q = deque(((n, 0),))
graph = [0] * 100001
print(DFS(q,m,graph))