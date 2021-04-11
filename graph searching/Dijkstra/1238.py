import heapq
import sys
input=sys.stdin.readline
N, M, X = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    y, x, t = map(int,input().split())
    graph[y].append((t,x))

def Dijkstra(start):
    queue = []
    arr = [float('inf')]*(M+1)
    arr[start] = 0
    heapq.heappush(queue,(0, start))
    while queue:
        distance, node = heapq.heappop(queue)
        if arr[node] < distance:
            continue
        for w, next_node in graph[node]:
            dis = distance + w
            if dis < arr[next_node]:
                arr[next_node] = dis
                heapq.heappush(queue,(dis, next_node))
    return arr

result = [[] for _ in range(N+1)]
for i in range(1, N+1):
    result[i] = Dijkstra(i)

output = []
for i in range(1, N+1):
    output.append(result[i][X]+result[X][i])
print(max(output))