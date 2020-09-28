def multiply(num1, num2):
    len_1 = len(num1)
    len_2 = len(num2)
    result = []
    index = -1
    final_result = 0
    for i in range(len_1 - 1, -1, -1):
        count = 0
        res = ""
        index += 1
        for j in range(len_2 - 1, -1, -1):
            product = int(num1[i]) * int(num2[j]) if count == 0 else int(num1[i]) * int(num2[j]) + count
            count = product // 10
            product_in = product % 10
            res += str(product_in)
            if j == 0 and count > 0:
                res += str(count)
        res = res[::-1]
        res += '0'*(index)
        result.append(res)
    for i in range(len(result)):
        final_result += int(result[i])

    return final_result

if __name__ == "__main__":
    nums1 = "0"
    nums2 = "0"
    print(multiply(nums1,nums2))
