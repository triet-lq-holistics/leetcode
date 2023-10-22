def permute(self, nums: List[int]) -> List[List[int]]:
        """
        base case:
            len(prefix) == len(nums): add into ans  and return ans
        recurrence: 
            for loop each item in  suffix: 
                call recursion:
                    - new suffix = current suffix - current item
                    - new prefix = current prefix + current item
        """

        def helper(prefix, suffix, ans):
            if len(prefix) == len(nums):
                ans.append(prefix)
                return ans 
            
            for idx, val in enumerate(suffix):
                new_prefix = prefix + [val]
                new_suffix = suffix[:idx] + suffix[idx+1:]
                ans = helper(new_prefix, new_suffix, ans)
            
            return ans 
        
        return helper([], nums, [])