def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            - sorted array to avoid duplication
            - pass if current item == prev item to avoid the re-computation

        """
        candidates = sorted(candidates)

        def helper(prefix, suffix, ans, total):
            if total < target:
                return ans 
            
            if sum(prefix) == target:
                ans.append(prefix[:])
                return ans
            
            elif sum(prefix) > target:
                return ans
            
            prev = -1
            for idx, val in enumerate(suffix):
                if val != prev:
                    prefix.append(val)
                    ans = helper(prefix, suffix[idx+1:], ans, total)
                    prefix.pop()
                    prev = val
                total -= val
            
            return ans 
        
        return helper([], candidates, [], sum(candidates))