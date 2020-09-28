def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    seq = []
    list = []
    if root is None:
        return seq
    list.append(root)
    layer = 0
    while(len(list) > 0):
        temp = []
        if layer % 2 == 0:
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
            layer += 1
        elif layer % 2 == 1:
            length_layer = len(list)
            temp_list = list[::-1]
            for i in range(length_layer):
                root = list[0]
                temp.append(root.val)
                del list[0]
                root = temp_list[i]
                if root.left is not None:
                    list.append(root.left)
                if root.right is not None:
                    list.append(root.right)
            seq.append(temp)
            layer += 1
    return seq


        
        