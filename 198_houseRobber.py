def rob(self, nums: List[int]) -> int:
        '''
            - Base case will be first and second house
            - Get maximum between last recursion state, or the 2nd preceeding recursion state + current val
        '''

        
        if len(nums) == 1:
            return nums[0]
        
        arr = [0] * len(nums)
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])

        for i in range(2, len(arr)):
            arr[i] = max(arr[i-1], arr[i-2] + nums[i])
        
        return arr[-1]

def rob(self, nums: List[int]) -> int:
        '''
            - Get maximum between last recursion state, or the 2nd preceeding recursion state + current val
            - Base case will be first and second house
        '''

        cache = {} 
        def dp(idx):
            if idx == 0:
                return nums[0]
            elif idx == 1:
                return max(nums[0], nums[1])
            elif idx in cache:
                return cache[idx]
            cache[idx] = max(dp(idx-1), dp(idx-2) + nums[idx])
            
            return cache[idx]
        
        return dp(len(nums) - 1)