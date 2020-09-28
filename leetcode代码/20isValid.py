def isValid(s:'str') -> 'bool':
    if s == "":
        return True
    char_list = []
    for char in s:
        if char =='(' or char == '[' or char == '{':
            char_list.append(char)
        elif char ==')':
            if len(char_list) and char_list[-1]=='(':
                char_list.pop()
            else:
                return False
        elif char == ']':
            if len(char_list) and char_list[-1]=='[':
                char_list.pop()
            else:
                return False
        elif char == '}':
            if len(char_list) and char_list[-1]=='{':
                char_list.pop()
            else:
                return False
    if len(char_list) == 0:
        return True
    else:
        return False

if __name__=="__main__":
    s = "()[]{}"
    t = isValid(s)
    print(t)
            


