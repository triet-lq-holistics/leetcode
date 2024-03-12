def numIslands(self, grid: List[List[str]]) -> int:
        '''
        - go through each item, then recursively loop thru each child (bottom and right) if it's equal to 1 
        - base case: out of scope or equal to 0  
        '''

        
        def traverse(row, col):
            grid[row][col] = '0' 
            if row + 1 < len(grid) and grid[row+1][col] == '1':
                traverse(row + 1, col)
            
            if col + 1 < len(grid[0]) and grid[row][col + 1] == '1':
                traverse(row, col+1)
            
            if col - 1 >= 0 and grid[row][col - 1] == '1':
                traverse(row, col-1)
            
            if row - 1 >= 0 and grid[row - 1][col] == '1':
                traverse(row - 1, col)
        
        count = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    traverse(row, col)

        return count    
