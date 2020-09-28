import sys
n = sys.stdin.readline().split(" ")
N = int(n[0])
M = int(n[1])
val_list = sys.stdin.readline().strip().split(" ")
dp = [[0 for i in range(N)]  for j in range(N)]
count = 0
for i in range(N):
    val_list[i] = int(val_list[i])
    if val_list[i] % M == 0:
        count += 1
        dp[i][i] = 0
    else:
        dp[i][i] = val_list[i] % M
for substring in range(2, N+1):
    for i in range(0, N-substring+1):
        j = i + substring -1
        if (dp[i][j-1] + val_list[j]) % M == 0:
            count += 1
            dp[i][j] = 0
        total_sum = dp[i][j - 1] + val_list[j]
        entra = total_sum % M
        if entra != 0:
            dp[i][j] = entra
print(count)
