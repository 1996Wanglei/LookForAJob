def deleteDuplicates(self, head):
    if head is None:
        return
    if head.next is not None and head.val == head.next.val:
        while (head.next is not None and head.val == head.next.val):
            head = head.next
        return self.deleteDuplicates(head.next)
    if head.next is not None and head.val != head.next.val:
        head.next = self.deleteDuplicates(head.next)
    return head

def deleteDuplicates(self, head):
