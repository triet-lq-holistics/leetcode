def numDecodings(self, s: str) -> int:
        '''
        - go from start to end 
        - for each recursion, 
            - call recursion on curr value
            -  check if current + next <= 26, call recursion on this case 
        - base case: 
            - when i == len(s) or (curr value = 0) then return 0 
            - when i == len(s) - 1 then return 1
        '''
        
        cache = {}
        def dp(i):
            if i == len(s):
                return 1 
            elif s[i] == '0': 
                return 0
                
            elif cache.get(i):
                return cache[i]
            
            count1 = dp(i+1)
            count2 = dp(i+2) if ((i+1) < len(s) and int(s[i] + s[i+1]) <= 26) else 0

            cache[i] = count1 + count2
            return cache[i]
        
        return dp(0)
