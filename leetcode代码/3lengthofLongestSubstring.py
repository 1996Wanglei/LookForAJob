def length(s):
    str = ''  
    max_count = 0
    for i in range(len(s)):
        if s[i] not in str:
            str +=  s[i]
        else:
            if max_count < len(str):
                max_count = len(str)
            str = str[str.index(s[i])+1:]
            str += s[i]
    if max_count < len(str):
        max_count = len(str)
    return max_count

if __name__=="__main__":
    s = "aab"
    c = length(s)
    print(c)

            

