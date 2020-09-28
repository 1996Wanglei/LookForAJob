import sys
hash_1 = {'9': '5', '8': '6', '7':'1', '6':'8', '5': '3', '3': '5', '2':'3', '1':'7', '0':'6'}
hash_2 = {'5':'9', '6':'8', '1':'7', '3':'5'}
for line in sys.stdin:
    str = line.strip()
    left = 0
    right = len(str)-1
    own_str = str
    flag1 = 0
    flag2 = 0
    index_left = 0
    index_right = len(str)-1
    while(left < right):
        print(1)
        if str[right] == '4':
            right -= 1
        elif flag1 == 0:
            flag1 = 1
            index_right = right
        if str[left] != '5' or str[left] != '6' or str[left] != '1' or str[left] != '3':
            left += 1
        elif flag2 == 0:
            flag2 = 1
            index_left = left
        if flag2 == 1 and flag1 == 1:
            break
    if flag1 ==0 or flag2 == 0:
        print(int(str))
    else:
        res = ""
        for i in range(len(str)):
                if i == index_left:
                    res += hash_2[str[index_left]]
                elif i == index_right:
                    res += hash_1[str[index_right]]
                else:
                    res += str[i]
        print(res)

