import sys
input = sys.stdin.readline
N = int(input())
liq = sorted(list(map(int,input().split())))
ans = [sys.maxsize, 0, 0, 0]
for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        tmp = abs(liq[left] + liq[right] + liq[i])
        if ans[0] > tmp:
            ans = [tmp, liq[left], liq[right], liq[i]]
        elif ans[0] <= tmp:
            left += 1
        else:
            right -= 1
print(ans[3], ans[1], ans[2])