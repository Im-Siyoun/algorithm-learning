N, d, k, c = map(int,input().split())
a = []
b = []
count = 0
for i in range(N):
    tmp = int(input())
    a.append(tmp)
i, j = 0, 0
while True:
    if count == k:
        if len(b) > len(result):
            result = b
            j += 1
    else:
        if a[j] in b:
            b.pop(0)
            i += 1
        else:
            b.append(a[j])
            j += 1
    