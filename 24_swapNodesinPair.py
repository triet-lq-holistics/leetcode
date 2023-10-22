def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
        Cut the link between first and second, and recursively update the first.next
        Return second (as the new first)
    """
    def helper(head):
        if not head or not head.next:
            return head
        
        second = head.next # tmp = 2
        first = head 
        
        first.next = helper(first.next.next)
        second.next = first 
        
        return second
    
    return helper(head)