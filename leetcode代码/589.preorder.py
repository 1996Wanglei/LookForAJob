# def preorder(root):
#         seq = []
#         stack = []
#         if root is None:
#             return seq
#         stack.append(root)
#         while(len(stack)):
#             temp_stack = []
#             root = stack.pop()
#             seq.append(root.val)
#             if root.children is not None:
#                 for children in root.children:
#                     # print(children.val)
#                     temp_stack.append(children)
#                 temp_stack.reverse()
#             stack.extend(temp_stack)
#         return seq
