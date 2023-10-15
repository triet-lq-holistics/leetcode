def maxArea(self, height: List[int]) -> int:
        """
        width = difference between 2 index 
        maxArea = width * height = diff * min(height between 2 index) 

        naive
        - nested for loop, get the area of each pair then compare to max

        2-pointer naively
        1. pointer left and right
        2. store max item of the array
        3. while loop, once done comparing the maxArea, 
            if the maxArea >= maxItem * (curDiff - 1), then return maxArea rightaway
            if the next item of one side is bigger than the other one, then we decide to move to the other side
        """
        maxAmount = 0
        left = 0 
        right = len(height) - 1 
        maxVal = max(height)

        while left < right:
            width = right - left
            
            currAmount = width * min(height[left], height[right])
            maxAmount = max(maxAmount,currAmount)

            if maxAmount >= maxVal * (width - 1):
                return maxAmount
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1 
        
        return maxAmount