
def isPalindrome(x):
    x_str = str(x)
    y_str = ""
    for i in x_str:
        y_str = i + y_str
    count = 0
    for i in range(len(x_str)):
        if x_str[i] == y_str[i]:
            count += 1
    if count == len(x_str):
        print("true")
        #return 'true'
    else:
        print("false")
        #return 'false'

if __name__=="__main__":
    x = 1
    a = isPalindrome(x)
