def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Declare the num counters  (1: 3, 3: 1, 2: 2)
        2. Declare a  max heap 
        3. Loop thru the num counters, and dump each value to the heap
        4. Control the heap allowing only k elements at max 
        """
        
        counter = Counter(nums)
        
        maxHeaps = []
        
        for key, value in counter.items():
            if len(maxHeaps) < k: 
                heapq.heappush(maxHeaps, (value, key))
            else:
                heapq.heappushpop(maxHeaps, (value, key))
        
        return [num for _, num in maxHeaps]