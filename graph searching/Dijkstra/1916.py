import heapq
import sys
input=sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    y, x, w = map(int,input().split())
    graph[y].append((w,x))
a, b = map(int,input().split())

def Dijkstra(start):
    arr = [float('inf')]*(N+1)
    arr[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        distance, node = heapq.heappop(queue)
        if arr[node] < distance:
            continue
        for cost, next_node in graph[node]:
            dis = distance + cost
            if dis < arr[next_node]:
                arr[next_node] = dis
                heapq.heappush(queue, (dis, next_node))
    return arr

print(Dijkstra(a)[b])