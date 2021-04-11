import sys
N = int(input())
H = sorted(list(map(int,input().split())))
ans = sys.maxsize
i, j = 0, 1
while j < N:
    tmp = abs(a[j]-a[i])
    if tmp < ans:
        ans = tmp
    elif tmp >= ans:
        j += 1
        i += 1
print(ans)