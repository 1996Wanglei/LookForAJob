

def sink_min(num_list, root):
    length = len(num_list)
    while 1: 
        if 2 * root + 1 < length:
            child = 2 * root + 2 if 2 * root +2 < length and num_list[2 * root +2] < num_list[2 * root +1] else 2 * root +1  # find the small child node
            if num_list[root] > num_list[child]:  #exchange the parent node and the child if the parent node bigger than child node 
                num_list[root], num_list[child] = num_list[child], num_list[root]
                root = child
            else:
                break
        else:
            break
                # sink(num_list, child)  # continue to adjust the new heap

def sink_max(num_list, root, length):
    # while 1:
        if root * 2 + 1 < length:
            child = 2 * root +2 if 2 * root +2 < length and num_list[2*root+2] > num_list[2*root+1] else 2*root +1
            if num_list[child] > num_list[root]:
                num_list[child], num_list[root] = num_list[root], num_list[child]
            sink_max(num_list,child, length)

def main(num_list):
        for i in range(len(num_list) // 2 -1, -1, -1):
            sink_max(num_list, i, len(num_list))
        for i in range(len(num_list)-1, 0, -1):
            num_list[0], num_list[i] = num_list[i], num_list[0]
            sink_max(num_list, 0, i)
            print(num_list[0])
        #print(num_list.pop(0))

if __name__ == "__main__":
    num_list = [1, 8, 23, 7 ,-4,18,23,42,37,2]
    main(num_list)