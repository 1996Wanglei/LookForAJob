def levelOrder(self, root: 'Node') -> List[List[int]]:
    seq = []
    list = []
    if root is None:
        return seq
    list.append(root)
    while (len(list) > 0):
        temp = []
        length = len(list)
        for i in range(length):
            root = list[0]
            temp.append(root.val)
            del list[0]
            if root.children is not None:
                for children in root.children:
                    list.append(children)
        seq.append(temp)
    return seq