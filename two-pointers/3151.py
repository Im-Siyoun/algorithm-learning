N = int(input())
A = list(map(int,input().split()))
count = 0
for a in range(0, N):
    if a > N-2:
        break
    for b in range(a+1, N):
        if b > N-1:
            break
        for c in range(b+1, N):
            if c > N:
                break
            elif (A[a] + A[b] + A[c] == 0):
                count += 1
print(count)