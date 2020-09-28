#_*_ coding:UTF-8 _*_
index1= {0: "零",
         1: "一",
         2: "二",
         3: "三",
         4: "四",
         5:  "五",
         6: "六",
         7: "七",
        8:"八",
        9:"九",
}
index2 = ["十","百","千","万","十万","百万","千万"]

a= 195080
index3 = []
index4 = []
j = len(str(a))-2
for i in range(len(str(a))):
    b = a%10
    index3.append(b)
    a = a//10
index3.reverse()
result = ""

print(j)
for i in index3:
    print(i)
    result = result + index1[i]
    result = result + index2[j]
    j -= 1

print(result)
print(index3)



