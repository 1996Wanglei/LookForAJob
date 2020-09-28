def isPalindrome(s):
    if s == "":
        return True
    str = s.lower()
    stack_1 = []
    # stack_2 = []
    for i in range(len(str)):
        if (str[i] <= "z" and str[i] >= "a") or (str[i] >= "0" and str[i] <= "9"):
            stack_1.append(str[i])
    print(stack_1)
    i = 0
    j = len(stack_1) - 1
    while (i < j):
        i += 1
        j -= 1
        if stack_1[i] != stack_1[j]:
            return False
        else:
            continue
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))