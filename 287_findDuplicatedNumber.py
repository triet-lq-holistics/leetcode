def findDuplicate(self, nums: List[int]) -> int:
        """
        length = n +1
        range = [1,n]

        Floyd's algorithm
        1. Declare slow and fast pointer (torture and hare)
        2. Run while loop until fast == slow
        3. Set slow position back to the beginning point while remain the curr fast position
        4. Set fast speed equal to slow speed
        5. Run while loop again until fast meet slow, then return slow|fast
        """

        slow, fast = 0, 0 

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break 
        
        slow = 0 

        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return slow