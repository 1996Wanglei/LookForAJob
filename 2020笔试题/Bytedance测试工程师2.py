
    def getIntersectionNode(headA, headB):
        head_1 = headA
        head_2 = headB
        length_1 = 0
        length_2 = 0
        if head_1.next == None or head_2.next == None:
            return None
        length_1 += 1
        length_2 += 1
        while(head_1.next):
            head_1 = head_1.next
            length_1 += 1
        while(head_2.next):
            head_2 = head_2.next
            length_2 += 1
        if head_1.val != head_2.val:
            return None
        else:
            length_diff =  length_1- length_2 if length_1 > length_2 else length_2-length_1
            head_3 = headA
            head_4 = headB
            if length_1 > length_2:
                while(length_diff):
                    head_3 = head_3.next
                    length_diff -= 1
            else:
                while(length_diff):
                    head_4 = head_4.next
                    length_diff -= 1
            while(True):
                if head_3.val != head_4.val:
                    head_3 = head_3.next
                    head_4 = head_4.next
                else:
                    return head_3