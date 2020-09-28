
def maxArea(height):
    low = 0
    high = len(height) -1
    max_Area = 0
    while(low < high):
        reauslt = height[low] if height[low] < height[high] else height[high]
        max_Area = max(max_Area, reauslt*(high-low))
        if height[low] < height[high]:
            low += 1
        else:
            high -= 1
    return max_Area

if __name__ =="__main__":
    c = [1,2,4,3]
    s = maxArea(c)
    print(s)