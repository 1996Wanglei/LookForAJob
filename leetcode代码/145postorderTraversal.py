def postorderTraversal(self, root: TreeNode) -> List[int]:
    seq = [] 
    stack = [] 
    if root is None:
        return seq
    while((root is not None)|(len(stack) > 0 )):
        if root is not None:
            seq.append(root.val)  # first visit root node
            stack.append(root)
            root = root.right # second visit rightchild node
        else:
            root = stack.pop()
            root = root.left # third visit leftchild node
    # beacause we visit by order that root,rightchild,left,
    # so we should reverse the final result
    return seq[::-1]

def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        pre = None
        cur = root
        seq = []
        stack = []
        while(cur !=None or len(stack) > 0):
            while(cur !=None):
                stack.append(cur)
                cur = cur.left
            if (len(stack) > 0):
                cur = stack.pop()
                if (cur.right == None or pre == cur.right):
                    seq.append(cur.val)
                    pre = cur
                    cur = None
                else:
                    stack.append(cur)
                    cur = cur.right
        return seq

