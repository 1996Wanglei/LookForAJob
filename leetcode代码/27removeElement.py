def removeElement(nums,val):
    c = {}
    count = 0
    for i in nums:
        if i != val:
            c.setdefault(i,0)
            c[i] += 1
            count += 1
    j = count
    for key in c:
        for i in range(0,c[key]):
            nums[count-1] = key   
            count -=1
    return j
