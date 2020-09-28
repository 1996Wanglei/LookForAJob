import sys
for line in sys.stdin:
    K = int(line.strip().split()[0])
    n = int(line.strip().split()[1])
    a = []
    for i in range(K):
        a.append(1)
    for j in range(K, n+1):
        temp = 0
        for m in range(j-K, j):
            temp = temp + a[m] % 397
        a.append(temp)
    print(a[n])