def convert(s, numsRows):
    length = len(s)
    if numsRows == 1:
        return s
    str = ""
    start_list = [i for i in range(numsRows)]
    for i in range(numsRows):
        start = start_list[i]
        flag = 0
        while(True):
            if start < length:
                str += s[start]
                if i == 0 or i == numsRows-1:
                    start += 2*(numsRows-1)
                else:
                    if flag == 0:
                        start += 2*(numsRows-i-1)
                        flag =1
                    else:
                        start += 2 * i
                        flag = 0
            else:
                break
    return str

if __name__ == "__main__":
    s = "LEETCODEISHIRING"
    print(convert(s, 3))