def trap(height):
    left = [0 for _ in range(len(height))]
    right = [0 for _ in range(len(height))]
    for i in range(1, len(height)):
        left[i] = max(left[i-1], height[i-1])
    for i in range(len(height)-2, -1, -1):
        right[i] = max(right[i+1], height[i+1])

    sum = 0
    print(left)
    print(right)
    for i in range(len(height)):
        axis = min(left[i], right[i])
        sum  += max(0,(axis-height[i]))
    return sum

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))