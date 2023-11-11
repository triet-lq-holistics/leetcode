def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        1. For each recursion, loop thru wordDict check if it matches the first n words of the curStr 
        2. If matches, then call recursion again, if it's true then return true 
        3. base case: if i == len(s) 
        3. After loop finish, return false
        '''

        cache = [None] * len(s) 

        def dp(i):
            if i == len(s):
                return True 
            
            elif cache[i] is not None:
                return cache[i]
            
            for word in wordDict:
                if word == s[i:i+len(word)]: 
                    cache[i] = dp(i+len(word))
                    if cache[i]:
                        return True
            
            return False
        
        return dp(0)

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Check if any word in wordDict match with any word in s starting at the current index. If match then we check the succeeding words
        
        Iterative: 
            - base case: len(s) = True
            - check if there's anyword that starts at current index 
            - if it's true, then check the next word's state if it's true as well (which we should've already calculated)
        '''

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for idx in range(len(s)-1, -1, -1):
            for word in wordDict:
                if len(word) <= len(s[idx:]) and word == s[idx:idx+len(word)] and dp[idx+len(word)]:
                    dp[idx] = True
        
        return dp[0]

