def rotateRight(head, k):
    if head == None:
        return None
    head_pointer = head
    length = 0
    while(head_pointer):
        head_pointer = head_pointer.next
        length += 1
    head_pointer = head
    k = k % length
    if k == 0:
        return head
    diff_length = length - k
    while(diff_length-1):
        diff_length -= 1
        head_pointer = head_pointer.next
    head_pointer2 = head_pointer.next
    final_head = head_pointer2
    head_pointer.next = None
    while(head_pointer2.next):
        head_pointer2 = head_pointer2.next
    head_pointer2.next = head
    return final_head
