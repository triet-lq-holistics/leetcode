def maxProfit(self, prices: List[int]) -> int:
        '''
        - if sell on one day, cannot buy on following day
        - cannot buy and sell on the same day
        -> can buy on one day, and sell the following day

        first buy: loop thru each of the item
        latter buy: buy item with at least 2 idx away 
        after buy, you gotta sell. After sell, you gotta buy

        action:
        - 0: buy
        - 1: sell

        1. Loop thru each item, and call dp on it (idx, action)
        2. Base case: idx == length: return 0 
        3. If buy: return max(dp(idx, sell) for each following item) - current_val
        4. If sell: return max(dp(idx, buy) for each following item except the next item) + current_val
        5. Store into cache, state = idx, action
        '''

        # action:
        # - 0: buy
        # - 1: sell
        
        cache = {}
        def dp(idx, action):
            if idx >= len(prices):
                return 0
            if (idx, action) in cache:
                return cache[(idx, action)]
            
            elif action == 0:
                cache[(idx, action)] = max([dp(next_idx, 1) for next_idx in range(idx+1, len(prices)+1)]) - prices[idx]
            else:
                cache[(idx, action)] = max([dp(next_idx, 0) for next_idx in range(idx+2, len(prices)+2)]) + prices[idx]
            
            return cache[(idx, action)]

        
        return max([dp(idx, 0) for idx in range(len(prices)+1)])
