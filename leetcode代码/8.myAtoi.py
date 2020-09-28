def myAtoi(str: str) -> int:
    str = str.strip()
    flag = ""
    if str[0] == "+" or str[0] == "-":
        flag = str[0]
        str = str[1::]
    if ord(str[0]) >= 48 and ord(str[0]) <= 57:
        integer = []
        for i in range(len(str)):
            if ord(str[i]) >= 48 and ord(str[i]) <= 57:
                integer.append(int(str[i]))
            else:
                break
        transf_integer = 0
        for i in range(len(integer)):
            if i == 0:
                transf_integer = integer[i]
                continue
            transf_integer *= 10
            transf_integer += integer[i]
            if transf_integer > (2 ** 31 -1) and (flag == "+" or flag == ""):
                return 2 ** 31 -1
            elif transf_integer > (2 ** 31) and flag == "-":
                return -2 **31
        if flag == "+" or flag == "":
            return transf_integer
        elif flag == "-":
            return (0-transf_integer)
    else:
        return 0;

if __name__ == "__main__":
    test = "2147483648"
    ss = myAtoi(test)
    print(ss)