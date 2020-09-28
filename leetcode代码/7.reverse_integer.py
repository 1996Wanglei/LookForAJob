
def reverse(x):
    tmp = []
    flag1 = 1
    if x < 0:
        x *= -1
        flag1 = -1
    if -10<x<10:
        return x*flag1
    flag = 1
    while(flag):
        count = x % 10
        tmp.append(count)
        x = x // 10
        if x < 10:
            flag = 0
            tmp.append(x)
    # print(tmp)
    newx,counts = (0,0)
    for i in range(len(tmp)):
        if tmp[i] != 0:
            counts = i
            break
    # print(counts)
    for j in range(counts, len(tmp)):
        newx += tmp[j]
        if j != len(tmp)-1:
            newx *= 10
    if -2**31<newx*flag1<2**31-1:
        return newx*flag1
    else:
        return 0


if __name__=="__main__":
    x = 1534236469
    tmp = reverse(x)
    print(tmp)
