def preorderTraversal(self, root: TreeNode) -> List[int]:
    seq = []
    stack = []
    if root is  None:
        return seq
    while((root is not None) | (len(stack) > 0)):
        if root is not None:
            seq.append(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right
    return seq