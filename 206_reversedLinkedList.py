def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head   
        prev = None

        while curr: 
            next = curr.next
            
            curr.next = prev
            prev = curr
            curr = next
        
        return prev 


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            each recursion, clone curr of the curr.next, then assign next of curr node to prev node, then call recursion on the clone
        """

        def helper(prev, curr):
            if not curr:
                return prev 

            next = curr.next
            curr.next = prev 

            return helper(curr, next)

        return helper(None, head)
