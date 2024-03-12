def maxProduct(self, nums: List[int]) -> int:
        maxP = nums[0]
        minP = nums[0]
        res = nums[0]

        for num in nums[1:]:
            tempMax = max(num, num*maxP, num*minP)
            minP = min(num, num*maxP, num*minP)
            maxP = tempMax

            res = max(res, maxP)
        
        return res
            
