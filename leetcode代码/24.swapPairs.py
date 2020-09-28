class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def swapPairs(head):
    if head != None and head.next != None:
        next = head.next
        head.next = swapPairs(next.next)
        next.next = head
        return next
    return head

if __name__ == "__main__":
    head = ListNode(0)
    head_pointer = head
    head_pointer2 = head
    for i in range(1, 10):
        temp = ListNode(i)
        head_pointer.next = temp
        head_pointer = head_pointer.next
    # swapPairs(head_pointer2.next)
    next = head.next
    while(next):
        print(next.val)
        next = next.next