def conbinationSum(candidates, target):
    length = len(candidates)
    result = []
    candidates.sort()
    temp = []
    sum = 0
    DFS(0, candidates, target, sum, result, temp)
    return result

def DFS(index,cadidate,target,sum,reauslt,temp):
    length = len(cadidate)
    if sum == target:
        reauslt.append(temp.copy())
        return
    if index == length or sum > target:
        return
    temp.append(cadidate[index])
    sum += cadidate[index]
    DFS(index, cadidate, target, sum, reauslt, temp)
    temp.pop()
    sum -= cadidate[index]
    DFS(index+1, cadidate, target, sum, reauslt, temp)

if __name__ == "__main__":
    candidates = [0,0,0]
    target = 0
    c = conbinationSum(candidates, target)
    print(c)