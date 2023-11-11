def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        1. declare cache 
        2. for each recursion, loop thru each suceeding item of the current indx, 
        3. If the succeeding value is smaller than the last recursion value, then we call recursion on that idx
        4. base case: when it reach the end of the array
        - arg: idx
        - return: len of increseing sequence
        '''

        cache = {}
        def dp(i):
            if i == len(nums):
                return 0
            elif i in cache:
                return cache[i]
            
            local_min = float('inf')
            res = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i] and nums[j] < local_min:
                    print(f'local_min {local_min} nums[i] {nums[i]} nums[j] {nums[j]}')
                    local_min = nums[j]
                    res = max(res, dp(j))
            cache[i] = res + 1 
            
            return cache[i]
        
        return max([dp(i) for i in range(len(nums))])
