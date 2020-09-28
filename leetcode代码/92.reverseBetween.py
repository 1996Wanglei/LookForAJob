def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    nullnode = ListNode(-1)
    nullnode.next = head
    pre = nullnode
    for i in range(m - 1):
        pre = pre.next
    cur = pre.next
    mnode = pre.next
    for i in range(m, n + 1):
        temp = cur.next  # 保存m+1结点
        cur.next = pre.next  # m+1结点的尾指针指向m结点
        pre.next = cur  # m-1结点的尾指针指向 m+1结点
        cur = temp  # 移到m+1结点
    mnode.next = cur  # m结点指向n+1结点
    return nullnode.next

