import sys
N, M = map(int,input().split())
A = []
for i in range(N):
    tmp = int(input())
    A.append(tmp)
A.sort()
ans = sys.maxsize
i, j = 0, 0
while j < N and i<N:
    tmp = A[j]-A[i]
    if A[j] - A[i] < M:
        j += 1
        continue
    else:
        i += 1
    ans = min(ans, tmp)
print(ans)