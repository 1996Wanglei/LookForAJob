def longestCommonPrefix(strs: 'List[str]') -> 'str':
    if len(strs) == 0:
        str = ""
        return str
    strs.sort(key=len)
    short_list = []
    if strs[0] == "":
        str = ""
        return str
    for i in range(len(strs[0])):
        tmp=strs[0][i]
        short_list.append(tmp)
        flag = 0
        for j in range(len(strs)):
            if strs[j][i] != tmp:
                flag = 1
            if flag and len(short_list)==0:
                str = ""
                return str
            elif flag and len(short_list) > 0:
                str = "".join(short_list[:-1])
                return str
        if flag == 0 and i == len(strs[0])-1:
            str = "".join(short_list)
            return str

if __name__ =="__main__":
    s = ["flow","flow","floe"]
    str = longestCommonPrefix(s)
    print(str)
            

