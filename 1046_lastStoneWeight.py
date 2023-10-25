def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        - Make stones into max heap
        - Each turn I will pop 2 stones out and follow the formula
        - While loop and when the heap has only 1 item left
        '''
        # Max heap
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, x-y)
        
        return 0 if not stones else -stones[0]
            