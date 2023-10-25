import heapq

class Solution:
    """
    215. Kth Largest Element in an Array
    https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/

    Tag: heap
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            heap: max heap and pop until nums <= k 
        """
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        
        return heapq.heappop(nums)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        quickselect:
            - pick a pivot (last index)
            - for loop + pointer, swap pointer to current val if current val < pivot
            - swap pivot with pointer's value 
            - quickselect on leftside if current pointer < k, right side if > k, and return val if it's = k 
        """

        def quickselect(l, r):
            pointer, pivot = l, nums[r]

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[pointer], nums[i]  = nums[i], nums[pointer]
                    pointer += 1
            
            nums[pointer], nums[r] =  pivot, nums[pointer]

            rank = len(nums) - pointer
            if rank < k: return quickselect(l, pointer-1)
            elif rank > k: return quickselect(pointer+1, r)
            else: return pivot
        
        return quickselect(0, len(nums) - 1)
