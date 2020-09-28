def count(n):
    d = {}
    for i in range(1, 31):
        d.setdefault(i, "")
    d[1] = '1'
    d[2] = '11'
    for i in range(3, 31):
        count = 0
        tmp_case = ""
        tmp = d[i-1][0]
        for j in range(len(d[i-1])):
            if tmp == d[i-1][j]:
                count += 1
            else:
                tmp_case = tmp_case+str(count)+str(tmp)
                tmp = d[i-1][j]
                count = 1
            if j == (len(d[i - 1]) - 1):
                tmp_case = tmp_case + str(count) + str(tmp)
        d[i] = tmp_case
    return d[n]

if __name__ == "__main__":
    count()