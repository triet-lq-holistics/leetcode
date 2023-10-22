def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums = sorted(nums)

        def helper(prefix, suffix):
            nonlocal ans 
            if prefix not in ans:
                ans.append(prefix[:])
            
            for idx, val in enumerate(suffix):
                prefix.append(val)
                helper(prefix, suffix[idx+1:])
                prefix.pop()
        
        helper([], nums)
        return ans