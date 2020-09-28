import sys
for line in sys.stdin:
    str_n = line.strip()
    state = 1
    res_stack = []
    state_stack=[]
    for i in range(len(str_n)):
        if len(res_stack) and str_n[i] == res_stack[-1]:
            res_stack.append(str_n[i])
            state += 1
        else:
            if state >= 3:
                while(state != 0):
                    res_stack.pop()
                    state -= 1
                if len(res_stack) and str_n[i] == res_stack[-1]:
                    state = state_stack[-1]
            else:
                state_stack.append(state)
                state = 0
            res_stack.append(str_n[i])
            state += 1
    if state >= 3:
        while(state != 0):
            res_stack.pop()
            state -= 1
    res = "".join(res_stack)
    print(res)