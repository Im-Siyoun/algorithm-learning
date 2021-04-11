N, M = map(int,input().split())
Card = list(map(int,input().split()))
output, CS = list(), list()
def full(o, p):
     o = 0;p += 1
la = 0
for v in range(N):
    for l in range(N):
        for i in range(N):
            if i != l and l != v and i != v:
                output.append([Card[i],Card[l],Card[v]])
                if v == len(Card):
                    full(v, l)
                elif l == len(Card):
                    full(l, i)
for d in range(len(output)):
    CS.append(output[d][0]+output[d][1]+output[d][2])
for e in range(len(CS)):
    if la < CS[e] <= M:
        la = CS[e]
print(la)