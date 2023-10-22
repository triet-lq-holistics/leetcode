def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            piles: banana
            h: time(h)
            k: bananas per hour 

            k will range between min - max of the piles 

        """

        def enough_time(k):
            duration = 0 
            for pile in piles:
                duration += ceil(pile/k)
            
            return duration <= h


        low, high = 1, max(piles)
        while low < high:
            k = low + (high-low)//2
            
            # if qualify (koko has more sparetime after done eating or koko has completed eating)
            # we will try lower the bar ~ lower the high pointer by setting high down to the middle pointer 
            if enough_time(k):
                high = k 
            
            # if not qualify, we're raising the bar 
            # since k is not working, we exclude current k by assign low as k = 1 
            # this also works when we try to lower the bar when koko found a good time but not minimum yet, so we try to lower the bar as low as possible, until it's not qualify (mostly low and high will have a difference of 1) ->  set low = k + 1 ~ low = high at this point. Hence it will break the loop and we are allowed to return low here
            else:
                low = k + 1
            
        return high


                
                # 1+2+3+4= 10 > 8 
                # k = 3, but 4 is the target => increase k 