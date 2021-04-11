from collections import deque
F, S, G, U, D = map(int,input().split())
visit = [0] * (F+1)
queue=deque()
def BFS(start):
    button = 1
    queue.append((start, button))
    visit[start] = button
    while queue:
        floor, button = queue.popleft()
        button += 1
        for i in (floor+U, floor-D):
            if 0<i<=F and (visit[i] == 0 or visit[i] > button):
                queue.append((i, button))
                visit[i] = button

BFS(S)
if visit[G] == 0:
    print('use the stairs')
else:
    print(visit[G]-1)