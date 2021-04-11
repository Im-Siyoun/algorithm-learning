import heapq
import sys
input=sys.stdin.readline
N, M = map(int,input().split())
adj = [[]for i in range(N+1)]
for i in range(M):
    y, x, w = map(int,input().split())
    adj[y].append([w,x])
    adj[x].append([w,y])

def d(start):
    arr = [float('Inf') for _ in range(N+1)]
    arr[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        distance, now_vertex = heapq.heappop(queue)
        if arr[now_vertex] > distance:
            continue
        for cost, node in adj[now_vertex]:
            dis = distance + cost
            if dis < arr[node]:
                arr[node] = dis
                heapq.heappush(queue, [dis, node])
    return arr
print(d(1)[N])