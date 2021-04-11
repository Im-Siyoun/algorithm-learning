N, S  = map(int,input().split())
a = list(map(int,input().split()))
low, high = 0, 0
tmp = a[0]
answer = float('inf')
while low!=N:
    if S <= tmp:
        answer = min(answer, high - low+1)
        tmp -= a[low]
        low += 1
    else:
        if high == N-1:
            tmp -= a[low]
            low += 1
        else:
            high += 1
            tmp += a[high]
if answer == float('inf'):
    print(0)
else:
    print(answer)