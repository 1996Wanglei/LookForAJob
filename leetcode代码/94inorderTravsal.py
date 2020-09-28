def inorderTraversal(self, root: TreeNode) -> List[int]:
    seq = []
    stack = []
    if root is None:
        return seq
    while((root is not None) || (len(stack) > 0)):
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            seq.append(root.value)
            root = root.right
    return seq
