def deleteDuplicates(self, head: ListNode) -> ListNode:
    head_pointer = head
    self.delete(head_pointer)
    return head


def delete(self, head):
    if head is None:
        return
    if head.next is not None and head.val != head.next.val:
        self.delete(head.next)
    if head.next is not None and head.val == head.next.val:
        # print(1)
        head.next = head.next.next
        self.delete(head)