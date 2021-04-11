import sys
input=sys.stdin.readline
N = int(input())
a = sorted(map(int,input().split()))
i, j = 0, N-1
tmp = [20000000000, 0, 0]
while i != j:
    tmp1 = abs(a[j] + a[i])
    if tmp1 < tmp[0]:
        tmp = [tmp1, a[i], a[j]]
    if abs(a[j]) > abs(a[i]):
        j -= 1
    else:
        i += 1
print(tmp[1], tmp[2])