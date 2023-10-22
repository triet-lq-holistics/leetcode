def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        - We can treat this one as a turtle-rabbit problem
        1. Set 2 pointers at the start of linkedlist
        2. 1 pointer will move faster than the other one (2 nodes per loop vs 1 node per loop)
        3. Once the 2 pointers meet, then it's a circle. Otherwise it's not 
        """

        turtle = head 
        rabbit = head 

        while turtle and rabbit: 
            turtle = turtle.next
            rabbit = rabbit.next
            
            # Return false if there's zero node ahead of rabbit
            # Return false early to avoid TypeError 
            if not rabbit:
                return False
            
            rabbit = rabbit.next

            if turtle == rabbit:
                return True
        
        return False
