def searchMatrix(matrix, target: int) ->bool:
    length_row = len(matrix)
    if length_row == 0:
        return False
    length_col = len(matrix[0])
    if length_col == 0:
        return False
    left = 0
    right = length_row-1
    while(left <= right):  # 搜索矩阵的第一列，定位可能的区间
        mid = left + ((right-left)//2)
        if matrix[mid][0] > target:
            right = mid - 1
        elif matrix[mid][0] < target:
            left = mid + 1
        else:
            return True
    last_integer = length_col -1
    #print(right, left)
    if right< 0:   #  如果target小于矩阵第一个元素
        return False
    #  target介于right指向的那一行最后一个元素，小于left指向的那一行第一个元素，并且left 要小于矩阵的行数
    elif target > matrix[right][last_integer] and left < length_row and target < matrix[left][0]:
        return False 
    #  target大于矩阵的行数， target大于right指向的行数最后一个元素
    elif left <= length_row and target > matrix[right][last_integer]:
        return False
    #  搜索指定的right行
    else:
        left_col = 0
        right_col = length_col-1
        # print(length_col)
        while(left_col <= right_col):
            mid_col = left_col + ((right_col - left_col)//2)
            print((right_col - left_col))
            if matrix[right][mid_col] >= target:
                right_col = mid_col-1
            else:
                left_col = mid_col +1
        return True if matrix[right][right_col+1] == target else False

if __name__ == "__main__":
    matirx = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 3
    Is = searchMatrix(matirx, target)
    print(Is)