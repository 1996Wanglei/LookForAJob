#题目描述：字符串str="1(2(3,4(,5)),6(7,))"表示一棵二叉树，其中A（B，C）表示A为根结点，B和C为A的左右子节点。根据字符串输出二叉树的中序遍历。

# 思路，用栈来保存父节点，利用方向标识来标识当前节点在左子树上还是右子树上。
# 如果匹配到了左括号，说明开始构建左子树，把方向标识置为true，把字符串前面的值的节点入栈。
# 如果匹配到了","说明左子树构建完成了，把方向标识置为false
# 如果匹配到了右括号，说明开始构建右子树或者向上回溯，这时需要将方向标识置为false，并且将栈顶的值出栈，因为当前的右子树已经构建完毕，需要回溯到父节点的父节点
# 如果匹配到了值，构建结点，


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

def str2Tree(string):
    child_flag = True
    if len(string) == 0:
        return ""
    stack = []

    # stack.append(string[0])
    node = TreeNode(string[0])
    root = node
    for i in range(1,len(string)):
        if string[i] == "(":
            stack.append(node)
            child_flag = True
        elif string[i] == ",":
            child_flag = False
        elif string[i] == ")":
            child_flag = False
            stack.pop()
        else:
            node = TreeNode(string[i])
            if child_flag:
                stack[-1].left = node
            else:
                stack[-1].right = node
    print(last_search(root))

# def mid_search(root):
#     if root is None:
#         return
#     mid_search(root.left)
#     print(root.val)
#     mid_search(root.right)

def mid_search(root):
    if root is None:
        return 
    stack = []
    while(root is not None or len(stack) > 0):
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.val)
            root = root.right

def fir_search(root):
    if root is None:
        return
    stack = []
    while(root is not None or len(stack) > 0):
        if root is not None:
            print(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right

def last_search(root):
    stack = []
    pre = None
    seq = []
    cur = root
    while(cur is not None or len(stack) > 0):
        while(cur is not None):
            stack.append(cur)
            cur = cur.left
        if len(stack) > 0:
            cur = stack.pop()
            if cur.right is None or pre == cur.right:
                seq.append(cur.val)
                pre = cur
                cur = None
            else:
                stack.append(cur)
                cur = cur.right
    return seq

def level_search(root):
    if root is None:
        return 
    queue = []
    queue.append(root)
    result = []
    while(len(queue)):
        layer = []
        nums_node = len(queue)
        for i in range(nums_node):
            root = queue.pop(0)
            layer.append(root.val)
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
        result.append(layer.copy())
    print(result)




if __name__ == "__main__":
    string = "1(2(3,4(,5)),6(,7)"
    str2Tree(string)
    


            



