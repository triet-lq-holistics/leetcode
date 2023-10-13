def maxProduct(self, nums: list[int]) -> int:
        """
        - cum product should not have an odd number of negative value
        - cum product can have an even number of negative value -> positive value 
        - Need to ignore the negative prefix if the suffix is positive

        1. ignore negative prefix if suffix is positive
        2. include the ngative prefix if suffix is negative 

        Whenever the cum sum is negative 
            1. store the current cum sum to the negative_prefix var 
            2. if the negative_prefix var already has a value, then cumsum = cumsum * negative_prefix, and negative_prefix = None 


        - proceed as normal if cumsum is  positive
        - Store a maxPositive and minNegative of the prefix
        """
        curMin, curMax = 1, 1
        res = float('-inf')


        for num in nums:
            tmp_min = num*curMin
            curMin = min(num*curMax, tmp_min, num)
            curMax = max(num*curMax, tmp_min, num)

            res = max(res, curMax)

        return res 
