matrix = [[0,0,0,0,0,0,0],
                 [0,0,1,0,0,0,0],
                 [0,1,0,1,1,0,0],
                 [0,0,1,0,0,1,1],
                 [0,0,1,0,0,0,0],
                 [0,0,0,1,0,0,1],
                 [0,0,0,1,0,1,0]]

def DFS(start):
    visit = []
    stack = []
    stack.append(start)
    visit.append(start)
    while stack:
        now_vertex = stack.pop()
        print(now_vertex, end='')
        for i in range(7):
            if matrix[now_vertex][i] == 1 and not i in visit:
                stack.append(i)
                visit.append(i)

def DFS1(start, visit):
    print(start, end='')
    visit.append(start)
    for i in range(7):
        if matrix[start][i] == 1 and not i in visit:
            DFS1(i, visit)
    return

def BFS(start): 
    visit = []
    queue = []
    queue.append(start)
    visit.append(start)
    while queue:
        now_vertex = queue.pop(0)
        print(now_vertex, end='')
        for i in range(7):
            if matrix[now_vertex][i] == 1 and not i in visit:
                queue.append(i)
                visit.append(i)

DFS(1)
print()
DFS1(1, [])
print()
BFS(1)
print()