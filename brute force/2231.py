N = int(input())
M = 0
l = []
for a in range(N):
    for i in range(len(str(a))):
        M += int((str(a))[i])
    Q = M + a
    if Q == N:
        l.append(a)
    M = 0
if len(l) >= 2:
    l.sort
    print(l[0])
elif len(l) == 0:
    print('0')
else:
    print(l[0])