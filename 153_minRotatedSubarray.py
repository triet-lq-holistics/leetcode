def findMin(self, nums: list[int]) -> int:
        """
        if the arr is  identical to the original arr,
             then the middle number is always smaller than the first num
            and  bigger than the last num
            [first] < mid < [last] 
            -> return the first num 
        elif mid > first_num
            first = mid 
            mid = (high + low) / 2 
        elif mid < first_num 
            high = mid 
            mid = ...
        """
        
        low = 0 
        high = len(nums) - 1 
        
        while (high-low) > 1: 
            mid = low + ((high - low) // 2) # 2 
            if nums[low] < nums[mid] < nums[high]: 
                return nums[low]
            elif nums[mid] > nums[low]: 
                low = mid
            elif nums[mid] < nums[low]: 
                high = mid 
        
        return min(nums[low], nums[high])