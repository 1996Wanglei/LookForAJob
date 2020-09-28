def isSymmetric(root):
    if root is None:
        return True
    seq = []
    list = []
    list.append(root)
    while (len(list)):
        length = len(list)
        for i in range(length):
            root = list[0]
            del list[0]
            if root is None:
                seq.append(-1)
                continue
            seq.append(root.val)
            list.append(root.left)
            list.append(root.right)
        r = len(seq) - 1
        l = 0
        while (l < r):
            if seq[l] == seq[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        seq = []
    return True

def isSyemetric(root):
    if root is None:
        return True
    self.search(root.left, root.right)


def search(self, left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val == right.val:
        return self.search(left.right, right.left) and self.search(left.left, right.right)
    else:
        return False