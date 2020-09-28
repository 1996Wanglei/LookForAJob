def combinationSum2(candidates,target):
    result = []
    temp = []
    sum = 0
    candidates.sort()
    DFS(0, target, sum, candidates, temp, result)
    return result


def DFS(index, target, sum, candidate, temp, result):
    if sum == target:
        if temp not in result:
            result.append(temp.copy())
            return
        else:
            return
    if sum > target or index == len(candidate):
        return
    temp.append(candidate[index])
    sum += candidate[index]
    DFS(index+1, target, sum, candidate, temp, result)
    temp.pop()
    sum -= candidate[index]
    DFS(index+1, target, sum, candidate, temp, result)

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    result = combinationSum2(candidates, target)
    print(result)