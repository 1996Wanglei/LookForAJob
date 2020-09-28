def longestPalindrome(s):
        length = len(s)
        if s == "":
            return s
        dp = [[0 for i in range(length)] for j in range(length)]
        max_length = 0
        count = 1
        for i in range(length):
            dp[i][i] = 1
            if i < length -1:
                if s[i] == s[i+1]:
                    dp[i][i+1] = 1
                    #dp[i+1][i] = 1
                    count = 2
        if length < 3:
            if count == 2:
                return s
            elif dp[0][0] == 1:
                return s[0]
        for len_substring in range(3, length+1): # 枚举每个子串可能的长度
            for i in range(length+1-len_substring):
                j = i+len_substring-1
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
        index_i = 0
        index_j = 0
        for i in range(length):
            for j in range(length):
                if dp[i][j] == 1:
                    count = j - i
                    if count > max_length:
                        max_length = count
                        index_i = i
                        index_j = j
        return s[index_i:index_j+1]

if __name__=="__main__":
    c = 'bbb'
    s = longestPalindrome(c)
    print(s)