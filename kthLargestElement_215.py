import heapq

class Solution:
    """
    215. Kth Largest Element in an Array
    https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/

    Tag: heap
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            Push eac k number into the heapq, then pop the smallest
            keep doing to the end of the list
            then return the final heap smallest number in the heap
        """
        heap = nums[:k]
        heapq.heapify(heap)
        
        for idx in range (k, len(nums)):
            heapq.heappush(heap, nums[idx])
            heapq.heappop(heap)
        
        return heapq.heappop(heap)

