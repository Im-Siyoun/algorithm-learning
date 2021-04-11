import sys
sys.setrecursionlimit(10**5)
F, S, G, U, D = map(int,input().split())
visit = [0] * (F+1)
global can
can = False
def DFS(start, button):
    visit[start] = button
    button = visit[start] + 1
    if start == G:
        print(button)
        global can
        can = True
    for i in (start + U, start - D):
        if 0<i<=F and not visit[i]:
                DFS(i, button)

DFS(S, 0)
if not can:
    print('use the stairs')