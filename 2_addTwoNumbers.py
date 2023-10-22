def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Naive:
            1. Store each val in each list in a string
            2. Convert 2 strings to int and add to a num
            3. Convert num to string and revert
            4. Create new linkedlist correspoding to string and return
        """    

        # Store each val in each list in a string    
        s1 = ""
        s2 = ""
        while l1:
            s1 += str(l1.val)
            l1 = l1.next

        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        
        # Add 2 number, convert to string then revert
        num = int(s1[::-1]) + int(s2[::-1])
        s = str(num)[::-1]

        # Add digit to linkedlist 
        ans = ListNode()
        dummy = ListNode()
        dummy.next = ans

        for idx, digit in enumerate(s): 
            ans.val = digit 
            ans.next = ListNode()
            
            if idx < len(s) - 1:
                ans = ans.next
            else:
                ans.next = None

        return dummy.next