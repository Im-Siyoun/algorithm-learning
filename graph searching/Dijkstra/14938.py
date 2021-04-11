import heapq
import sys
input=sys.stdin.readline
n, m, r = map(int,input().split())
area = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for i in range(r):
    a, b, l = map(int,input().split())
    graph[a].append((l,b))
    graph[b].append((l,a))

def Dijkstra(start):
    arr = [float('inf')]*(n+1)
    arr[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        distance, node = heapq.heappop(queue)
        if arr[node] < distance:
            continue
        for w, next_node in graph[node]:
            dis = distance + w
            if dis < arr[next_node] and dis <= m:
                arr[next_node] = dis
                heapq.heappush(queue, (dis, next_node))
    return arr

result = []
for i in range(1, n+1):
    count = 0
    tmp = Dijkstra(i)
    for l in range(0, n+1):
        if tmp[l] == float('inf'):
            continue
        else:
            count += area[l-1]
    result.append(count)
print(max(result))