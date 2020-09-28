def Decision(str):
    str = str.strip()
    last_chara = str[-1]
    punctuation = ""
    stack_1 = []
    isChara = False
    if (last_chara <= "Z" and last_chara>= "A") or (last_chara <= "z" and last_chara>= "a"):
        isChara = True
    if not isChara:
        punctuation = str[-1]
        str = str[:-1]
    temp = ""
    for i in range(len(str)):
        if str[i] != " ":
            temp += str[i]
            if i == len(str) -1:
                stack_1.append(temp)
        else:
            stack_1.append(temp)
            temp = ""
    target_str = ""
    for i in range(len(stack_1)-1, -1, -1):
        target_str += stack_1[i]
        if i != 0:
            target_str += " "
    if not isChara:
        target_str += punctuation
    return target_str

if __name__ == "__main__":
    source_str = "i love China! "
    print(Decision(source_str))