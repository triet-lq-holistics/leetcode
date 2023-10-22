def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        backtracking: add item to array in a for loop, until it reach the base case, then add array to ans.  Then remove that item and process the next one
        """

        ans = []
        def helper(arr, startIdx):
            ans.append(arr[:])
            
            for i in range(startIdx, len(nums)):
                arr.append(nums[i])
                helper(arr, i+1)
                arr.pop()
        
        helper([], 0)
        return ans