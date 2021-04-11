N = int(input())
n = 5000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
i, j = 0, 0
count = 0
while primes[i] <= N:
    l = i
    tmp = 0
    while l < j+1:
        tmp += primes[l]
        l += 1
    if tmp < N:
        j += 1
    elif tmp == N:
        count += 1
        i += 1
    elif tmp > N:
        i += 1
print(count)