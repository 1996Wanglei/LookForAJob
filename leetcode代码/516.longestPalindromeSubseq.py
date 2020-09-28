def longestPalindromeSubseq(s):
    length_string = len(s)
    dp = [[0 for _ in range(length_string)] for _ in range(length_string)]
    for i in range(length_string):
        dp[i][i] = 1
    for i in range(length_string-1, -1, -1):
        for j in range(i+1, length_string):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    max_length = 0
    for i in range(length_string):
        for j in range(length_string):
            if dp[i][j] > max_length:
                max_length = dp[i][j]
    return max_length

