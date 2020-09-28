def strStr(haystack,needle):
    len_needle = len(needle)
    len_haystack = len(haystack)
    index = 0
    if len_needle == 0:
        return index
    def getnext(length_pattern,pattern):
        j = - 1
        next = list(range(len_needle))
        next[0] = -1
        for i in range(1,length_pattern):
            while(j != -1 and pattern[i] != pattern[j+1]):
                j = next[j]
            if pattern[i] == pattern[j+1]:
                j += 1
            next[i] = j
        return next
    next = getnext(len_needle,needle)
    print(next)
    j = -1
    for i in range(len_haystack):
        while(j != -1 and haystack[i] != needle[j+1]):
            j = next[j]
        if haystack[i] == needle[j+1]:
            j += 1
        if j == len_needle -1:
            index = i + 1 - len_needle
            return index
    return -1
if __name__ == "__main__":
    a = "mississippi"
    b = "issip"
    index = strStr(a,b)
    print(index)