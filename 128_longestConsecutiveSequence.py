def longestConsecutive(self, nums: List[int]) -> int:
        """
        1. loop thru nums
        2. if lag of num is not in nums, then increment num and add to the temp sequence until then incremental value is not in nums 
        3. Compare longest with length of curr sequence
        """
        longest = 0
        nums = set(nums) 

        # O(N)
        for num in nums:
            if (num - 1) not in nums:
                curr = num 
                count = 0 
                while curr in nums: 
                    curr += 1 
                    count += 1 
                longest = max(longest, count)
        
        return longest
                