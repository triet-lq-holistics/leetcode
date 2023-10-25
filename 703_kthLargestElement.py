import heapq

class KthLargest:
    """naive:
        - sorted the init array
        - add: for loop thru the array, if the current val is larger than the new index, then store the idx, then rebuild the array using that idx, then store only last k elements 

        b-tree:
        - sort the array
        - 

        heap:
        - heapify the array
        - add new val to the array, and pop the smallest elements until it has k elements
        - pop and return top value of heap
    """
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k 

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]