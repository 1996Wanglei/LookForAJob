# 思路：给每个结点都加上标记，根节点的值为0，那么根节点的左孩子结点的值为-1，右孩子结点的值为1。
# 根结点左孩子的左孩子结点的值为-2，结点左孩子的右孩子结点的值为0.
# 应该先按照x坐标把 结点存起来，这个时候顺带也要把y坐标存起来，
# 我们然后按照x坐标排序，然后再检索出相同的y，把他们的值按大小排序，加入到


def verticalL0order(root):
    index_dic = {}
    queue = []
    if root is None:
        return
    queue.append(((0,0), root))
    while(len(queue)):
        nums_node = len(queue)
        for i in range(nums_node):
            index_node_pair = queue.pop(0)  
            if index_node_pair[0][0] not in index_dic:
                 # index_node_pair[0][0] 是x坐标，index_node_pair[0][1]是y坐标
                index_dic[index_node_pair[0][0]] = [[index_node_pair[0][1], index_node_pair[1].val]] 
            else:
                index_dic[index_node_pair[0][0]].append([index_node_pair[0][1],index_node_pair[1].val])
            if index_node_pair[1].left is not None:
                queue.append(((index_node_pair[0][0]-1,index_node_pair[0][1]-1), index_node_pair[1].left))
            if index_node_pair[1].right is not None:
                queue.append(((index_node_pair[0][0]+1,index_node_pair[0][1]-1), index_node_pair[1].right))
    
    final_result = []
    result = []
    sort_list = sorted(index_dic.items(), key = lambda x: x[0])
    for key, value in sort_list:
        dic_same_index = {}
        for i in range(len(value)):
            if value[i][0] not in dic_same_index:
                dic_same_index[value[i][0]] = [value[i][1]]
            else:
                dic_same_index[value[i][0]].append(value[i][1])
        for key, value in dic_same_index.items():
            if len(value) > 1:  # 相同的位置的结点大于了两个，排序
                value = sorted(value)
                result.extend(value)
            else:
                result.extend(value)
        final_result.append(result.copy())
        result = []
    return final_result

        
    
    

            
