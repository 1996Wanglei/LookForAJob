def intToRoman(num):
    index = [['', 'M', 'MM', 'MMM'],
             ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
             ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
             ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']]
    res = ""
    i = 4 - len(str(num))
    for number in str(num):
       res += index[i][int(number)]
       i += 1
    return res

if __name__ == "__main__":
    num = 990
    print(intToRoman(num))

