def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        '''
        cache = {}
        coins = sorted(coins)
        def dp(i, total):
            if total > amount:
                return float('inf')
            
            if total == amount:
                return 0 
            
            if cache.get((i, total)):
                return cache[(i,total)]
            
            cache[(i, total)] = min([dp(idx, total+coins[idx]) for idx in range(i, len(coins))]) + 1 
            return cache[(i, total)]
        
        res = dp(0, 0)
        return res if res != float('inf') else -1 
