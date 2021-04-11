from collections import deque
S = int(input())
arr = [0 for _ in range(1001)]
queue = deque()
def DFS(node, visit, time):
    time += 1
    start, clipboard = node
    if start == S:
        return time
    visit[start] = time
    if start*2 <= S*2:
        clipboard = start
        time += 1
        DFS([start+clipboard, clipboard], visit, time)
    if start != 1:
        DFS([start-1, clipboard], visit, time)
DFS([1, 0], arr, -1)