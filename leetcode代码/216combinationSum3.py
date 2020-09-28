def combinationSum3(k, n):
    result = []
    temp = []
    sum = 0
    length_temp = 0
    list = [1,2,3,4,5,6,7,8,9]
    DFS(0, list,n,k,length_temp,result,temp, sum)
    return result

def DFS(index, list, n, k, length_temp, result, temp, sum):
    if sum == n and length_temp == k:
        result.append(temp.copy())
        return
    if sum > n or length_temp > k or index >= len(list):
        return
    sum += list[index]
    temp.append(list[index])
    length_temp += 1
    DFS(index+1, list, n, k, length_temp, result, temp, sum)
    temp.pop()
    length_temp -= 1
    sum -= list[index]
    DFS(index + 1, list, n, k, length_temp, result, temp, sum)


if __name__ == "__main__":
    print(combinationSum3(2, 9))
