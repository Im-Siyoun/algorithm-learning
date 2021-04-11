import sys
input=sys.stdin.readline
N, S = map(int,input().split())
a = list(map(int,input().split()))
minlen = sys.maxsize
i, j = 0, 0
while j < N:
    tmp = 0
    for l in range(i,j+1):
        tmp += a[l]
    if tmp >= S:
        minlen = min(j+1-i, minlen)
        i += 1
    else:
        j += 1
if minlen == sys.maxsize:
    print(0)
else:
    print(minlen)