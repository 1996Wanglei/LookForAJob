def removeDuplicates(nums) -> int:
    c = {}
    for i in nums:
        c.setdefault(i,0)
        c[i] += 1
    j = 0
    for key in c:
        if c[key] >= 1:
            j += 1
    return j

if __name__=="__main__":
    nums = [1,1,2]
    a=removeDuplicates(nums)
    print(a)