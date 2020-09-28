def romanToint(s):
    index_dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    value_int=0
    for i,value in enumerate(s):
        if s[i] == 'V' and s[i-1] == 'I' and i > 0:
            value_int += 3
        elif s[i] == 'X' and s[i-1] == 'I' and i > 0:
            value_int += 8
        elif s[i] == 'L' and s[i-1] == 'X'and i > 0:
            value_int += 30
        elif s[i] == 'C' and s[i-1] == 'X'and i > 0:
            value_int += 80
        elif s[i] == 'D' and s[i-1] == 'C'and i > 0:
            value_int += 300
        elif s[i] == 'M' and s[i-1] == 'C'and i > 0:
            value_int += 800
        else:
            value_int += index_dic[s[i]]
    return value_int
if __name__=="__main__":
    s = "XXVII"
    x=romanToint(s)
    print(x)  
        
    
        

