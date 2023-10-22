def sortArray(self, nums: List[int]) -> List[int]:
        """
        Merge sort: Divide to sublist, then sort 2 sublists, then merge
        """
        if len(nums) == 1:
            return [nums[0]]
        
        partition = len(nums) // 2 
        
        left = self.sortArray(nums[:partition])
        right = self.sortArray(nums[partition:])

        l,r = 0,0
        ls = []
        while l < len(left) or r < len(right):
            if r >= len(right):
                ls.append(left[l]) 
                l += 1 
            elif l >= len(left):
                ls.append(right[r])
                r += 1
            elif left[l] <= right[r]:
                ls.append(left[l])
                l += 1
            else:
                ls.append(right[r]) 
                r += 1

        return ls