def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. Flatten the matrix to one array
        2. Binary search 
        """        

        arr = []
        for ls in matrix:
            arr.extend(ls)

        
        lo, hi = 0, len(arr) - 1

        while lo < hi:
            mid = lo + (hi-lo)//2

            if arr[mid] >= target:
                hi = mid 
            else:
                lo = mid + 1 
        
        return True if arr[lo] == target else False