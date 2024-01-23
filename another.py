def is_cycle(l1):

    fast = l1.head.next
    slow = l1.head.next

    while fast != None and slow != None:

        fast = fast.next.next
        slow = slow.next

        if(fast == slow):
            return True
        
    return False