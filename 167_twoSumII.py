def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Naive: 
        1. Create nested for loops 
        2. sum each pair of items, then compare to target

        two-pointers 
        1. Declare 2 pointers low and high
        2. if sum of low and high
            a. > target: decrease high
            b. < target: increase low 
        """
        
        low = 0 
        high = len(numbers) - 1 

        while low < high: 
            sm = numbers[low] + numbers[high] # 5 
            
            if sm == target:
                return [low+1, high+1]
            
            elif sm > target:
                high -= 1 
            else:
                low += 1 
        