N = int(input())
P, O, rank= [], [], []
c = 0
for i in range(N):
    w, h = map(int,input().split())
    P.append([w,h])
    rank.append(1)
for a in range(0,N):
    for b in range(0,N):
        if P[a][0] < P[b][0] and P[a][1] < P[b][1]:
            rank[a] += 1
for i in rank:
    print(i, end=' ')