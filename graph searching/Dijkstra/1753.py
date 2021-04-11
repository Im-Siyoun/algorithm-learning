import heapq
import sys
input=sys.stdin.readline
V, E = map(int,input().split())
adj = [[] for _ in range(V+1)]
s = int(input())
for i in range(E):
    y, x, w = map(int,input().split())
    adj[y].append((w,x))

def di(start):
    arr = [float('inf')]*(V+1)
    arr[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        distance, node = heapq.heappop(queue)
        if arr[node] < distance:
            continue
        for w, nex in adj[node]:
            dis = distance + w
            if dis < arr[nex]:
                arr[nex] = dis
                heapq.heappush(queue, [arr[nex], nex])
    return arr

tmp = di(s)
for i in range(1,V+1):
    print('INF' if tmp[i] == float('inf') else tmp[i])