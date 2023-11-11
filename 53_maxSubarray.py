def maxSubArray(self, nums: list[int]) -> int:
        """
        constraint metric: sum 
        numeric restriction: None 
        rules: take maximum sum 

        - leftmost and rightmost elmement always positive 
        -> Move from left to right 
        -> Calculate cumsum as we go
        -> if current cumsum is negative, then reset cumsum = 0 
        -> get the maximum between current cumsum and ans 
        """
        ans = 0 
        cumsum = 0

        for num in nums: 
            cumsum += num 
            if cumsum < 0:
                cumsum = 0 
            else:
                ans = max(ans, cumsum)

        if ans == 0:
            return max(nums)
        
        return ans 



def maxSubArray(self, nums: List[int]) -> int:
        """
        1. global max, subarray sum
        2. loop thru the array
        3. if current val > subarray sum, then replace subarray sum 
        4. compare to global max
        5. return global max
        """

        global_max = nums[0]
        local_sum = nums[0]
        for num in nums[1:]:
            local_sum = max(local_sum + num, num)
            global_max = max(global_max, local_sum)
        
        return global_max



