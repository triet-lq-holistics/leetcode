def getRow(self, rowIndex: int) -> List[int]:
        """
        Brute force with each row and col calling another recursion of other row col. Can be optimized using memoization (lru cache) 
        """
        
        lru = {}
        def helper(row, col):
            if col == 0 or row == 0 or row == col: 
                return 1 
            elif (row,col) in lru:
                return lru.get((row,col))
            
            val =  helper(row-1,col-1) + helper(row-1, col)
            lru[(row,col)] = val 

            return val
        
        ls = [1] * (rowIndex + 1)

        for i in range(1, len(ls)-1):
            ls[i] = helper(rowIndex, i)
        return ls
    