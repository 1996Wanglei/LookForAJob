def minDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    if root.left == None and root.right != None:
        return self.minDepth(root.right) + 1
    if root.right == None and root.left != None:
        return self.minDepth(root.left) + 1
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1