class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        
        return len(numsSet) < len(nums)
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        for num in nums:
            if cache.get(num):
                return True
            cache[num] = 1
        
        return False