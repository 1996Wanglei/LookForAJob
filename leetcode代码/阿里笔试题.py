import sys

n = int(sys.stdin.readline().strip())
print(n)
for k in range(n):
    #print(sys.stdin.readline().strip().split(" "))
    input_list = sys.stdin.readline().strip().split(" ")
    k = int(input_list[0])
    l = int(input_list[1])
    print(input_list)
    m = 0
    product = k*l
    for i in range(1,k+1):
        for j in range(1, l+1):
            if (i+j) % 2 != 0:
                m += 1
    if m == 0:
        print("0/1")
    else:
        n0 = product
        m0 = m
        print(n0, m0)
        while(product % m !=0):
            temp = product
            product = m
            m = temp % m
        m0 = int(m0/m)
        n0 = int(n0/m)
        print("{}/{}".format(m0, n0))
