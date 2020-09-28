def groupAnagrams(strs):
    result = {}
    for i in range(len(strs)):
        key = "".join(sorted(strs[i]))
        if key not in result:
            result[key] = [strs[i]]
        else:
            result[key].append(strs[i])
    return list(result.values())

if __name__ == "__main__":
    a = ["ray","cod","abe","ned","arc","jar","owl","pop","paw","sky","yup","fed","jul","woo","ado","why","ben","mys","den","dem","fat","you","eon","sui","oct","asp","ago","lea","sow","hus","fee","yup","eve","red","flo","ids","tic","pup","hag","ito","zoo"]
    print(groupAnagrams(a))