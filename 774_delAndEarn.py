def deleteAndEarn(self, nums: List[int]) -> int:
        '''        
        base case: if idx = 0, then return val 
        recurrence relation: 
        '''

        counter = Counter(nums)
        keys = sorted(list(counter.keys()))
        points = {key:key*val for key,val in counter.items()}
        cache = {}
        
        def dp(i): 
            num = keys[i]
            if i == 0:
                return points[num] 
            elif i == 1:
                return max(points[keys[i-1]], points[keys[i]]) if num - keys[i-1] == 1 else points[keys[i-1]] + points[keys[i]]
            
            elif cache.get(num):
                return cache[num]
            
            if num - keys[i-1] == 1:
                cache[num] = max(dp(i-2) + points[num], dp(i-1))
            else:
                cache[num] = dp(i-1) + points[num]

            return cache[num]
        
        return dp(len(keys) - 1)