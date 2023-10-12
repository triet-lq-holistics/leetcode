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