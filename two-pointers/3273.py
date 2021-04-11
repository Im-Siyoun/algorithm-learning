import sys
input=sys.stdin.readline
N = int(input())
a = sorted(map(int,input().split()))
x = int(input())
i, j = 0, N-1
count = 0
while i != j:
    tmp = a[i] + a[j]
    if tmp == x:
        count += 1
        i += 1
    elif tmp > x:
        j -= 1
    elif tmp < x:
        i += 1
print(count)