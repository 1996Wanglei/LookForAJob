def levelOrder(self, root: TreeNode) -> List[List[int]]:
    list = []
    seq = []
    if root is None：
        return seq
    list.append(root)
    while(len(list) > 0):
        temp = []
        length_layer = len(list)
        for i in range(length_layer):
            root = list[0]
            temp.append(root.val)
            del list[0]
            if root.left is not None:
                list.append(root.left)
            if root.right is not None:
                list.append(root.right)
        seq.append(temp)
    return seq


