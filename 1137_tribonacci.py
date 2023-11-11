def tribonacci(self, n: int) -> int:
        '''
        n = 0 -> 0
        n = 1 -> 1
        n = 2 -> 1

        base case: above n 
        recurrence relation: sum of the last 3 calc 
        '''

        cache = [None] * (n + 1)
        def dp(n):
            if n == 0: 
                return 0 
            elif n in (1,2):
                return 1 
            elif cache[n]:
                return cache[n]
            cache[n] = sum([dp(n-1), dp(n-2), dp(n-3)])
            return cache[n]
        
        return dp(n)