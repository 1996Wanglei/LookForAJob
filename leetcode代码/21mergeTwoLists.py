class Listnode:
    def __init__(self,x):
        self.val = x
        self.next = None

def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
    r = Listnode(0)
    head = r
    while l1 and l2:
        if l1.val <= l2.val:
            head.next = l1
            head = head.next
            l1 = l1.next
        else: 
            head.next = l2
            head = head.next
            l2 = l2.next
    if l1:
        while l1:
            head.next = l1
            head = head.next
            l1 = l1.next
    elif l2:
        while l2:
            head.next = l2 
            head = head.next
            l2 = l2.next
    head = r.next